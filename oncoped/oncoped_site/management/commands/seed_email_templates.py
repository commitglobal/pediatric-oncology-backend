from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

from oncoped_site.models import EmailTemplate

PATIENT_REQUEST_TEXT = """
Hi,

The request for patient "{{ pr.first_name }} {{ pr.last_name }}" was received with the following data:

First Name: {{ pr.first_name }}
Last Name: {{ pr.last_name }}
Birth Date: {{ pr.birth_date }}
Sex: {{ pr.get_sex_display }}
Address: {{ pr.address }}

Requester Type: {{ pr.get_institution_type_display }}
Organization Name: {{ pr.institution_name }}
Requester First Name: {{ pr.requester_first_name }}
Requester Last Name: {{ pr.requester_last_name }}
Requester Phone: {{ pr.requester_phone_number }}
Requester Email: {{ pr.requester_email }}

Diagnostic Class: {{ pr.get_diagnostic_class_display }}
{% if pr.known_complete_diagnostic %}
Complete Diagnostic: {{ pr.complete_diagnostic }}
Date Diagnosed: {{ pr.date_diagnosed }}
Diagnosing Institution Name: {{ pr.diagnosing_institution_name }}
{% else %}
General Problem Description: {{ pr.general_problem_description }}
{% endif %}

Tumor Type: {{ pr.get_tumor_type_display }}
Therapy Needs: {{ pr.get_therapy_needs_display }}

Thank you!
Pediatric Oncology Team

--- RO ---

Buna,

Cererea de inscriere a pacientului "{{ pr.first_name }} {{ pr.last_name }}" a fost primita cu urmatoarele date:

Prenume: {{ pr.first_name }}
Nume: {{ pr.last_name }}
Data de Naștere: {{ pr.birth_date }}
Sex: {{ pr.get_sex_display }}
Adresă: {{ pr.address }}

Tipul Solicitantului: {{ pr.get_institution_type_display }}
Nume Organizație: {{ pr.institution_name }}
Prenumele Solicitantului: {{ pr.requester_first_name }}
Numele Solicitantului: {{ pr.requester_last_name }}
Numărul de Telefon al Solicitantului: {{ pr.requester_phone_number }}
Email-ul Solicitantului: {{ pr.requester_email }}

Clasa de diagnostic: {{ pr.get_diagnostic_class_display }}
{% if pr.known_complete_diagnostic %}
Diagnostic Complet : {{ pr.complete_diagnostic }}
Data de diagnostic : {{ pr.date_diagnosed }}
Numele Instituției care a diagnosticat: {{ pr.diagnosing_institution_name }}
{% else %}
Descrierea problemei : {{ pr.general_problem_description }}
{% endif %}

Tipul Tumorii: {{ pr.get_tumor_type_display }}
Necesarul Terapeutic: {{ pr.get_therapy_needs_display }}

Va multumim!
Echipa Oncologie Pediatrica
"""


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--replace",
            action="store_true",
            help="Replace existing templates",
        )

    def handle(self, *args, **options):
        template, created = EmailTemplate.objects.get_or_create(template="patient_request")

        if created or options["replace"]:
            template.text_content = PATIENT_REQUEST_TEXT
            template.save()
