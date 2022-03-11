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
        exclude = [
            "medical_documents_checked",
            "current_clinical_status",
            "child_current_address",
            "child_current_city",
            "child_current_county",
            "child_current_country",
            "origin_medical_institution_name",
            "origin_medical_institution_contact_person",
            "origin_medical_institution_phone_number",
            "origin_medical_institution_email",
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
