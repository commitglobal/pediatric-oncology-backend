from django.contrib import admin
from dispatch.models import (
    Clinic,
    PatientRequest,
    PatientRequestFile,
    MedicalAssistance,
    LogisticAndSocialAssistance,
    Companion,
)
from import_export.admin import ImportExportModelAdmin
from django.db.models import TextField, Sum
from django.forms import Textarea
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _


admin.site.index_template = "admin/custom_admin_index.html"


def admin_index_custom_context(request):
    ctx = {}
    if request.path[3:] == "/admin/":
        patients_count_all = PatientRequest.objects.count()
        patients_assigned = PatientRequest.objects.filter(
            med_assistance__clinic__isnull=False
        ).count()
        patiens_unassigned = patients_count_all - patients_assigned

        ctx["count_patient_requests_all"] = patients_count_all
        ctx["count_patient_requests_assigned"] = patients_assigned
        ctx["count_patient_requests_unassigned"] = patiens_unassigned
        try:
            if patients_assigned:
                if patiens_unassigned:
                    ctx["patient_requests_assigned_percentage"] = int(
                        round((1 - (patiens_unassigned / patients_count_all)) * 100, 0)
                    )
                else:
                    ctx["patient_requests_assigned_percentage"] = 100
            else:
                ctx["patient_requests_assigned_percentage"] = 0
        except ZeroDivisionError:
            ctx["patient_requests_assigned_percentage"] = 0

        clinics_count = Clinic.objects.count()
        all_beds = (
            Clinic.objects.annotate(all_beds=Sum("available_beds"))
            .values_list("all_beds", flat=True)
            .first()
        ) or 0
        available_beds = all_beds - patients_assigned
        try:
            if all_beds:
                beds_occupation = int(round((1 - (available_beds / all_beds)) * 100, 0))
            else:
                beds_occupation = 100
        except ZeroDivisionError:
            beds_occupation = 0

        ctx["count_clinics"] = clinics_count
        ctx["count_clinics_all_beds"] = all_beds
        ctx["count_clinics_available_beds"] = available_beds
        ctx["count_clinics_beds_occupation"] = beds_occupation

    return ctx


class PatientRequestFileInLine(admin.TabularInline):
    model = PatientRequestFile
    extra = 1
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
        (
            None,
            {
                "fields": (
                    "transport_required",
                    "transport",
                    "transport_details",
                    "pick_up_location",
                    "contact_person",
                    "accommodation_required",
                    "accommodation_details",
                    "destination_asisting_entity_details",
                ),
                "classes": ("logistic-social-assistance",),
            },
        ),
    )


@admin.register(LogisticAndSocialAssistance)
class AdminLogisticAndSocialAssistance(admin.ModelAdmin):
    # Just to hide the model in admin...
    def get_model_perms(self, request):
        return {}


class CompanionInLine(admin.StackedInline):
    model = Companion
    extra = 1
    max_num = 5
    verbose_name_plural = _("Add Companion")


@admin.register(Companion)
class AdminCompanion(admin.ModelAdmin):
    # Just to hide the model in admin...
    def get_model_perms(self, request):
        return {}


@admin.register(Clinic)
class AdminClinic(ImportExportModelAdmin):
    list_display = [
        "tumor_type",
        "name",
        "city",
        "county",
        "address",
        "hospitalization_office_email",
        "hospitalization_office_phone_number",
        "head_of_dept_name",
        "head_of_dept_email",
        "dept_phone",
        "available_beds",
    ]

    list_display_links = [
        "tumor_type",
        "name",
    ]

    search_fields = [
        "tumor_type",
        "name",
        "city",
        "county",
    ]

    list_filter = [
        "tumor_type",
        "name",
        "city",
        "county",
    ]

    ordering = ("pk",)

    formfield_overrides = {
        TextField: {"widget": Textarea(attrs={"rows": 4, "cols": 63})},
    }


@admin.register(PatientRequest)
class AdminPatientRequest(ImportExportModelAdmin):
    def assigned_clinic(self, obj):
        clinic = obj.med_assistance.clinic
        if clinic:
            return mark_safe(
                f'<span style="font-weight: bold; color: green;">{clinic.name}, {clinic.city} ({clinic.county})</span>'
            )
        return mark_safe(
            '<i class="fas fa-times" style="font-weight: bold; color: red; font-size: 20px;"></i>'
        )

    assigned_clinic.short_description = _("Assigned Clinic")

    def requires_logistic_and_social_assistance(self, obj):
        transport = obj.logsol_assistance.transport_required
        accommodation = obj.logsol_assistance.accommodation_required
        if transport and not accommodation:
            return mark_safe(
                '<i class="fas fa-car-side" style="font-weight: bold; font-size: 20px;"></i>'
            )
        if accommodation and not transport:
            return mark_safe(
                '<i class="fas fa-house-user" style="font-weight: bold; font-size: 20px;"></i>'
            )
        if transport and accommodation:
            return mark_safe(
                (
                    '<i class="fas fa-car-side" style="font-weight: bold; font-size: 20px; margin-right: 10px;"></i>'
                    '<i class="fas fa-house-user" style="font-weight: bold; font-size: 20px;"></i>'
                )
            )
        return None

    requires_logistic_and_social_assistance.short_description = _(
        "Logistic & Social Assistance"
    )

    def number_of_companions(self, obj):
        companions = obj.companions.count()
        if companions:
            return mark_safe(
                '<i class="fas fa-male" style="font-weight: bold; font-size: 20px; margin-right: 10px;"></i>'
                * companions
            )

    number_of_companions.short_description = _("Companions")

    list_display = [
        "get_full_name",
        "age",
        "sex",
        "tumor_type",
        "estimated_arrival_dt",
        "assigned_clinic",
        "requires_logistic_and_social_assistance",
        "number_of_companions",
    ]
    list_display_links = ["get_full_name"]
    search_fields = ["first_name", "last_name", "tumor_type"]
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
        CompanionInLine,
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
