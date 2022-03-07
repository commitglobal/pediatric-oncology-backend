from django.contrib import admin
from dispatch.models import PatientRequest, PatientRequestFile
from import_export.admin import ImportExportModelAdmin
from django.db.models import TextField
from django.forms import Textarea
from django.utils.translation import gettext_lazy as _


class PatientRequestFileInline(admin.TabularInline):
    model = PatientRequestFile
    extra = 1
    show_change_link = True
    view_on_site = True
    verbose_name_plural = _("Upload Medical Files")


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

    inlines = [PatientRequestFileInline]

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
                    "address"
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
    )
