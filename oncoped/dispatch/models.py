from django.db import models
from multiselectfield import MultiSelectField
from django.utils.translation import gettext_lazy as _


DOCUMENT_TYPES_CHOICES = (
    ("PAS", _("Passport")),
    ("NID", _("National ID")),
)

SEX_CHOICES = (
    ("M", _("Male")),
    ("F", _("Female")),
    ("O", _("Other / Unspecified")),
)

TUMOR_TYPE_CHOICES = (("S", _("Solid")), ("H", _("Hemato")))

THERAPY_NEEDS_CHOICES = (
    ("CHE", _("Chemotherapy")),
    ("SUR", _("Surgical")),
    ("PAL", _("Palliative")),
    ("MON", _("Monitoring")),
    ("INV", _("Diagnostic Investigation")),
    ("SUT", _("Supportive Treatment")),
    ("RAD", _("Radiotherapy")),
    ("TRA", _("Transplant")),
)


# TODO Clinics Model
# contact details
# Available beds


class PatientRequest(models.Model):

    # Identification
    document_type = models.CharField(
        verbose_name=_("Document Type"),
        max_length=3,
        choices=DOCUMENT_TYPES_CHOICES,
        default="PAS",
        null=False,
        blank=False,
    )
    document_identification_number = models.CharField(
        verbose_name=_("Document Identification Number"),
        max_length=50,
        null=False,
        blank=False,
    )
    document_expiry_date = models.DateField(
        verbose_name=_("Document Expiry Date"),
        null=False,
        blank=False,
    )
    document_issuing_country = models.CharField(
        verbose_name=_("Document Issuing Country"),
        max_length=50,
        null=False,
        blank=False,
    )
    first_name = models.CharField(
        verbose_name=_("First Name"),
        max_length=100,
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        verbose_name=_("Last Name"),
        max_length=100,
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        verbose_name=_("Age"), null=False, blank=False
    )
    sex = models.CharField(
        verbose_name=_("Sex"),
        max_length=2,
        choices=SEX_CHOICES,
        default="PAS",
        null=False,
        blank=False,
    )

    # Requester
    requester_first_name = models.CharField(
        verbose_name=_("Requester First Name"),
        max_length=100,
        null=False,
        blank=False,
    )
    requester_last_name = models.CharField(
        verbose_name=_("Requester Last Name"),
        max_length=100,
        null=False,
        blank=False,
    )
    requester_phone_number = models.CharField(
        verbose_name=_("Requester Phone Number"),
        max_length=30,
        help_text=_("Please include country prefix e.g. +40723000123")
    )
    requester_is_medical_institution = models.BooleanField(
        verbose_name=_("Medical Institution"), default=False
    )
    medical_institution_name = models.CharField(
        verbose_name=_("Medical Institution Name"),
        max_length=250,
        null=True,
        blank=True,
        help_text=_("Fill in only if requester is a medical institution"),
    )

    # Medical Info
    complete_diagnostic = models.TextField(
        verbose_name=_("Complete Diagnostic"),
        help_text="Put some helful explanation here...",
        null=False,
        blank=False,
    )
    available_diagnostic = models.TextField(
        verbose_name=_("Available Diagnostic / Request Reason"),
        help_text="Put some helful explanation here...",
        null=False,
        blank=False,
    )
    tumor_type = models.CharField(
        verbose_name=_("Tumor Type"),
        max_length=2,
        choices=TUMOR_TYPE_CHOICES,
        default="S",
        null=False,
        blank=False,
    )
    therapy_needs = MultiSelectField(
        verbose_name=_("Therapy Needs"),
        choices=THERAPY_NEEDS_CHOICES,
        null=False,
        blank=False,
    )
    location = models.CharField(
        verbose_name=_("Child Location"),
        max_length=250,
        help_text=_("Where is the child at the moment of the request"),
        null=False,
        blank=False,
    )
    clinical_status = models.CharField(
        verbose_name=_("Clinical Status"),
        max_length=250,
        null=False,
        blank=False,
    )
    # TODO Foreign Key to clinics - with filter based on tumor type. not required, e.g. unassigned/assigned -> Important as it is done manually.

    # Logistical Info
    estimated_arrival_dt = models.DateTimeField(
        verbose_name=_("Estimated Arrival"), null=False, blank=False
    )
    redirect_info = models.TextField(
        verbose_name=_("Redirect Info"),
        help_text=_(
            "Redirection to a different specialty. Provide all info, including contact!"
        ),
    )
    is_direct_request = models.BooleanField(
        verbose_name=_("Direct Request"),
        default=False,
        help_text=_(
            "Patient has directly presented him/herself in the clinc without contact?"
        ),
    )

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return f"#{self.id} {self.get_full_name()} {self.age}{self.sex}"

    class Meta:
        verbose_name = _("Patient Request")
        verbose_name_plural = _("Patient Requests")