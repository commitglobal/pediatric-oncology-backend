from captcha.fields import ReCaptchaField
from crispy_forms.helper import FormHelper
from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from dispatch.models import PatientRequest


class PatientRequestForm(forms.ModelForm):
    captcha = ReCaptchaField(
        label="",
    )

    class Meta:
        model = PatientRequest
        fields = [
            # requester
            "requester_category",
            "institution_name",
            "requester_first_name",
            "requester_last_name",
            "requester_phone_number",
            "requester_email",
            # patient
            "first_name",
            "last_name",
            "birth_date",
            "sex",
            "birth_place",
            # diagnostic
            "known_complete_diagnostic",
            "complete_diagnostic",
            "date_diagnosed",
            "diagnosing_institution_name",
            "general_problem_description",
            "therapy_needs",
            "other_therapy_needs",
            # location
            "child_current_address",
            "child_current_city",
            "child_current_country",
        ]
        widgets = {
            "sex": forms.RadioSelect,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

        if not settings.RECAPTCHA_PUBLIC_KEY:
            del self.fields["captcha"]

        self.fields["therapy_needs"].label = _("What are the medical services the patient needs?")
