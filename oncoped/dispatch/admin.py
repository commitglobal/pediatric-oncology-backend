from django.contrib import admin
from dispatch.models import (
    PatientRequest,
    PatientRequestFile,
    MedicalAssistance,
    LogisticAndSocialAssistance,
)
from import_export.admin import ImportExportModelAdmin
from django.db.models import TextField
from django.forms import Textarea
from django.utils.translation import gettext_lazy as _


class PatientRequestFileInLine(admin.TabularInline):
    model = PatientRequestFile
    extra = 1
    show_change_link = True
    show_delete_link = True
    view_on_site = True
    verbose_name_plural = _("Upload Medical Files")


@admin.register(PatientRequestFile)
class AdminPatientRequestFile(admin.ModelAdmin):
    # Just to hide the model in admin...
    def get_model_perms(self, request):
        return {}


class MedicalAssistanceInLine(admin.StackedInline):
    model = MedicalAssistance

    verbose_name_plural = _("Add Medical Assitance")


@admin.register(MedicalAssistance)
class AdminMedicalAssistance(admin.ModelAdmin):
    # Just to hide the model in admin...
    def get_model_perms(self, request):
        return {}


class LogisticAndSocialAssistanceInLine(admin.StackedInline):
    model = LogisticAndSocialAssistance

    verbose_name_plural = _("Add Logistic & Social Assistance")

    fieldsets = (
        (None, {
            "fields": (
                "pick_up_location",
                "contact_person",
                "transport_required",
                "transport",
                "transport_details",
                "accommodation_required",
                "accommodation_details",
                "destination_asisting_entity_details",
            ),
            "classes": ("logistic-social-assistance",),
        }),
    )
    


@admin.register(LogisticAndSocialAssistance)
class AdminLogisticAndSocialAssistance(admin.ModelAdmin):
    # Just to hide the model in admin...
    def get_model_perms(self, request):
        return {}


@admin.register(PatientRequest)
class AdminPatientRequest(ImportExportModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "age",
        "sex",
        "tumor_type",
        "estimated_arrival_dt",
    ]
    list_display_links = [
        "first_name",
        "last_name",
    ]
    search_fields = ["first_name", "last_name", "tumor_type", "location"]
    list_filter = [
        "first_name",
        "last_name",
        "tumor_type",
    ]

    ordering = ("pk",)

    view_on_site = False

    inlines = [
        PatientRequestFileInLine,
        MedicalAssistanceInLine,
        LogisticAndSocialAssistanceInLine,
    ]

    formfield_overrides = {
        TextField: {"widget": Textarea(attrs={"rows": 4, "cols": 63})},
    }

    change_form_template = "admin/patient_request_admin.html"

    fieldsets = (
        (
            _("Identification"),
            {
                "fields": (
                    "document_type",
                    "document_identification_number",
                    "document_expiry_date",
                    "document_issuing_country",
                    "first_name",
                    "last_name",
                    "birth_date",
                    "age",
                    "sex",
                    "address",
                )
            },
        ),
        (
            _("Requester"),
            {
                "fields": (
                    "requester_first_name",
                    "requester_last_name",
                    "requester_phone_number",
                    "institution_type",
                    "institution_name",
                ),
            },
        ),
        (
            _("General Medical Info"),
            {
                "fields": (
                    "complete_diagnostic",
                    "available_diagnostic",
                    "tumor_type",
                    "therapy_needs",
                    "other_therapy_needs",
                    "clinical_status_comments",
                ),
                "classes": ("detalii-produs",),
            },
        ),
        (
            _("Child Location"),
            {
                "fields": (
                    "child_current_address",
                    "child_current_city",
                    "child_current_county",
                    "child_current_country",
                )
            },
        ),
        (
            _("Logistical Info"),
            {
                "fields": (
                    "estimated_arrival_dt",
                    "redirect_info",
                    "is_direct_request",
                )
            },
        ),
        (
            _("Origin Medical Institution"),
            {
                "fields": (
                    "origin_medical_institution_name",
                    "origin_medical_institution_contact_person",
                    "origin_medical_institution_phone_number",
                    "origin_medical_institution_email",
                )
            },
        ),
    )
