from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView

from dispatch.models import PatientRequest
from oncoped_site.forms import PatientRequestForm


class PatientRegisterRequestCreateView(SuccessMessageMixin, CreateView):
    template_name = "form.html"
    model = PatientRequest
    form_class = PatientRequestForm
    success_message = _("Thank you for registering the patient! The form you filled in has reached us.")

    def get_success_url(self):
        return reverse("patient_request_form")
