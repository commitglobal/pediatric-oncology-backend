from django.contrib import admin
from dispatch.models import PatientRequest
from import_export.admin import ImportExportModelAdmin
from django.db.models import TextField
from django.forms import Textarea
from django.utils.translation import gettext_lazy as _


@admin.register(PatientRequest)
class AdminPatientRequest(ImportExportModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "age",
        "sex",
        "tumor_type",
        "location",
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
        "location",
    ]

    ordering = ("pk",)

    view_on_site = False

    formfield_overrides = {
        TextField: {"widget": Textarea(attrs={"rows": 4, "cols": 63})},
    }

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
                    "age",
                    "sex",
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
                    "requester_is_medical_institution",
                    "medical_institution_name",
                ),
            },
        ),
        (
            _("Medical Info"),
            {
                "fields": (
                    "complete_diagnostic",
                    "available_diagnostic",
                    "tumor_type",
                    "therapy_needs",
                    "location",
                    "clinical_status",
                ),
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
