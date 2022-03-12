from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

from oncoped_site.models import EmailTemplate

PATIENT_REQUEST_TEXT = """
Hi,

The request for patient "{{ pr.first_name }} {{ pr.last_name }}" was received with the following data:

Requester Type: {{ pr.get_requester_category_display }}
{% if pr.institution_name %}Organization Name: {{ pr.institution_name }}{% endif %}
Requester First Name: {{ pr.requester_first_name }}
Requester Last Name: {{ pr.requester_last_name }}
Requester Phone: {{ pr.requester_phone_number }}
Requester Email: {{ pr.requester_email }}

First Name: {{ pr.first_name }}
Last Name: {{ pr.last_name }}
Birth Date: {{ pr.birth_date }}
Sex: {{ pr.get_sex_display }}

{% if pr.known_complete_diagnostic == "1" %}
Complete Diagnostic: {{ pr.complete_diagnostic }}
Date Diagnosed: {{ pr.date_diagnosed }}
Diagnosing Institution Name: {{ pr.diagnosing_institution_name }}
{% else %}
General Problem Description: {{ pr.general_problem_description }}
{% endif %}

What are the medical services the patient needs?
{{ pr.get_therapy_needs_display }}

{% if pr.other_therapy_needs %}Other Therapy Needs: {{ pr.other_therapy_needs }}{% endif %}

Child Current Address: {{ pr.child_current_address }}
Child Current City: {{ pr.child_current_city }}
Child Current Country: {{ pr.child_current_country }}

Thank you!
Ukraine Child Cancer Help Romania

--- RO ---

Buna,

Cererea de inscriere a pacientului "{{ pr.first_name }} {{ pr.last_name }}" a fost primita cu urmatoarele date:

Tipul Solicitantului: {{ pr.get_requester_category_display }}
{% if pr.institution_name %}
Denumire: {{ pr.institution_name }}
{% endif %}
Prenumele Solicitantului: {{ pr.requester_first_name }}
Numele Solicitantului: {{ pr.requester_last_name }}
Numărul de Telefon al Solicitantului: {{ pr.requester_phone_number }}
Email-ul Solicitantului: {{ pr.requester_email }}

Prenume pacient: {{ pr.first_name }}
Nume pacient: {{ pr.last_name }}
Data de Naștere: {{ pr.birth_date }}
Sex: {{ pr.get_sex_display }}

{% if pr.known_complete_diagnostic == "1" %}
Diagnostic Complet : {{ pr.complete_diagnostic }}
Data de diagnostic : {{ pr.date_diagnosed }}
Numele Instituției care a diagnosticat: {{ pr.diagnosing_institution_name }}
{% else %}
Descrierea problemei : {{ pr.general_problem_description }}
{% endif %}

Care sunt serviciile medicale de care are nevoie pacientului?
{{ pr.get_therapy_needs_display }}

{% if pr.other_therapy_needs %}Alte Nevoi terapeutice : {{ pr.other_therapy_needs }}{% endif %}

Adresa Curenta a pacientului: {{ pr.child_current_address }}
Orașul Curent al pacientului: {{ pr.child_current_city }}
Țara curentă a pacientului: {{ pr.child_current_country }}

Va multumim!
Ukraine Child Cancer Help Romania
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
