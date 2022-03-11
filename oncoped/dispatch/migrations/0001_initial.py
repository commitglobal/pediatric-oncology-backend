# Generated by Django 3.2.12 on 2022-03-11 11:14

import dispatch.models
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tumor_type', multiselectfield.db.fields.MultiSelectField(choices=[('S', 'Solid'), ('H', 'Hematologic')], max_length=3, verbose_name='Tumor Type')),
                ('therapy_services', multiselectfield.db.fields.MultiSelectField(choices=[('CHE', 'Chemotherapy'), ('SUR', 'Surgical'), ('PAL', 'Palliative'), ('MON', 'Monitoring'), ('INV', 'Diagnostic Investigation'), ('SUT', 'Supportive Treatment'), ('RAD', 'Radiotherapy'), ('TRA', 'Transplant'), ('OTH', 'Other')], max_length=35, verbose_name='Therapy Services')),
                ('name', models.CharField(max_length=150, verbose_name='Clinic Name')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('county', models.CharField(choices=[('AB', 'Alba'), ('AR', 'Arad'), ('AG', 'Argeș'), ('BC', 'Bacău'), ('BH', 'Bihor'), ('BN', 'Bistrița-Năsăud'), ('BT', 'Botoșani'), ('BV', 'Brașov'), ('BR', 'Brăila'), ('B', 'București'), ('BZ', 'Buzău'), ('CL', 'Călărași'), ('CS', 'Caraș-Severin'), ('CJ', 'Cluj'), ('CT', 'Constanța'), ('CV', 'Covasna'), ('DB', 'Dâmbovița'), ('DJ', 'Dolj'), ('GL', 'Galați'), ('GR', 'Giurgiu'), ('GJ', 'Gorj'), ('HR', 'Harghita'), ('HD', 'Hunedoara'), ('IL', 'Ialomița'), ('IS', 'Iași'), ('IF', 'Ilfov'), ('MM', 'Maramureș'), ('MH', 'Mehedinți'), ('MS', 'Mureș'), ('NT', 'Neamț'), ('OT', 'Olt'), ('PH', 'Prahova'), ('SM', 'Satu Mare'), ('SJ', 'Sălaj'), ('SB', 'Sibiu'), ('SV', 'Suceava'), ('TR', 'Teleorman'), ('TM', 'Timiș'), ('TL', 'Tulcea'), ('VS', 'Vaslui'), ('VL', 'Vâlcea'), ('VN', 'Vrancea')], max_length=3, verbose_name='County')),
                ('address', models.CharField(max_length=250, verbose_name='Address')),
                ('hospitalization_office_email', models.EmailField(max_length=254, verbose_name='Hospitalization Office Email')),
                ('hospitalization_office_phone_number', models.CharField(max_length=30, verbose_name='Hospitalization Office Phone Number')),
                ('head_of_dept_name', models.CharField(max_length=100, verbose_name='Head Of Department Name')),
                ('head_of_dept_email', models.EmailField(max_length=254, verbose_name='Head Of Department Email')),
                ('dept_phone', models.CharField(max_length=30, verbose_name='Department Phone Number')),
                ('available_beds', models.SmallIntegerField(default=0, verbose_name='Available Beds')),
            ],
            options={
                'verbose_name': 'Clinic',
                'verbose_name_plural': 'Clinics',
            },
        ),
        migrations.CreateModel(
            name='PatientRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('birth_date', models.DateField(verbose_name='Birth Date')),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other / Unspecified')], default='PAS', max_length=2, verbose_name='Sex')),
                ('address', models.CharField(max_length=250, verbose_name='Address')),
                ('institution_type', models.CharField(choices=[('MED', 'Medical Institution'), ('NGO', 'Non-Governmental Organization'), ('PER', 'Person'), ('COM', 'Company')], default='MED', max_length=3, verbose_name='Type')),
                ('institution_name', models.CharField(blank=True, help_text='Fill in only if requester is not a Person', max_length=250, verbose_name='Name')),
                ('requester_first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('requester_last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('requester_phone_number', models.CharField(help_text='Please include country prefix e.g. +40723000123', max_length=30, verbose_name='Phone Number')),
                ('requester_email', models.EmailField(max_length=254, verbose_name='Email')),
                ('diagnostic_class', models.CharField(blank=True, choices=[('LAMM', 'Leucemii, afecțiuni mieloproliferative și mielodisplazice'), ('LNR', 'Limfoame și neoplasme reticuloendoteliale'), ('SNCNII', 'SNC și neoplasme intracraniene și intraspinale'), ('NATCNP', 'Neuroblastom și alte tumori ale celulelor nervoase periferice'), ('R', 'Retinoblastom'), ('TR', 'Tumori renale'), ('TH', 'Tumori hepatice'), ('TMO', 'Tumori maligne ale oaselor'), ('SPMATE', 'Sarcoame de părți moi și alte țesuturi extraosoase'), ('TTNG', 'Tumori terofoblastice și neoplasme ale gonadelor'), ('ANMEMM', 'Alte neoplasme maligne epiteliale și melanoame maligne'), ('ANMN', 'Alte neoplasme maligne nespecificate')], max_length=10, verbose_name='Diagnostic Class')),
                ('known_complete_diagnostic', models.BooleanField(default=False, verbose_name='Complete Diagnostic Known')),
                ('complete_diagnostic', models.TextField(blank=True, verbose_name='Complete Diagnostic')),
                ('date_diagnosed', models.DateField(blank=True, null=True, verbose_name='Date Diagnosed')),
                ('diagnosing_institution_name', models.CharField(blank=True, max_length=150, verbose_name='Diagnosing Institution Name')),
                ('general_problem_description', models.TextField(blank=True, help_text="Describe the Child's medical issue", verbose_name='General Problem Description')),
                ('medical_documents_checked', models.BooleanField(default=False, verbose_name='Medical Documents Checked')),
                ('tumor_type', models.CharField(blank=True, choices=[('S', 'Solid'), ('H', 'Hematologic')], max_length=2, verbose_name='Tumor Type')),
                ('therapy_needs', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('CHE', 'Chemotherapy'), ('SUR', 'Surgical'), ('PAL', 'Palliative'), ('MON', 'Monitoring'), ('INV', 'Diagnostic Investigation'), ('SUT', 'Supportive Treatment'), ('RAD', 'Radiotherapy'), ('TRA', 'Transplant'), ('OTH', 'Other')], max_length=35, verbose_name='Therapy Needs')),
                ('other_therapy_needs', models.CharField(blank=True, max_length=250, verbose_name='Other Therapy Needs')),
                ('current_clinical_status', models.TextField(blank=True, verbose_name='Current Clinical Status')),
                ('child_current_address', models.CharField(blank=True, max_length=100, verbose_name='Child Current Address')),
                ('child_current_city', models.CharField(blank=True, max_length=100, verbose_name='Child Current City')),
                ('child_current_county', models.CharField(blank=True, max_length=100, verbose_name='Child Current County')),
                ('child_current_country', models.CharField(blank=True, max_length=100, verbose_name='Child Current Country')),
                ('estimated_arrival_dt', models.DateTimeField(blank=True, null=True, verbose_name='Estimated Arrival')),
                ('redirect_info', models.TextField(blank=True, help_text='Redirection to a different specialty. Provide all info, including contact!', verbose_name='Redirect Info')),
                ('is_direct_request', models.BooleanField(default=False, help_text='Patient has directly presented him/herself in the clinc without contact?', verbose_name='Direct Request')),
                ('origin_medical_institution_name', models.CharField(blank=True, max_length=150, verbose_name='Institution Name')),
                ('origin_medical_institution_contact_person', models.CharField(blank=True, help_text='Full Name of the contact person', max_length=150, verbose_name='Contact Person')),
                ('origin_medical_institution_phone_number', models.CharField(blank=True, help_text="Contact Person's phone number. Please include country prefix e.g. +40723000123", max_length=30, verbose_name='Phone Number')),
                ('origin_medical_institution_email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Patient Request',
                'verbose_name_plural': 'Patient Requests',
                'unique_together': {('first_name', 'last_name', 'birth_date')},
            },
        ),
        migrations.CreateModel(
            name='PatientRequestFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to=dispatch.models.patient_request_upload)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispatch.patientrequest')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalAssistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_status', models.CharField(choices=[('P', 'Case Pending'), ('R', 'Clinic is Ready for takeover'), ('T', 'Taken over by Clinic'), ('TP', 'Taken over previously, in person')], default='P', max_length=3, verbose_name='Case Status')),
                ('estimated_arrival_date', models.DateField(blank=True, null=True, verbose_name='Estimated Arrival Date')),
                ('hospitalization_start', models.DateField(blank=True, help_text='Only with confirmation from the receiving clinic!', null=True, verbose_name='Hospitalization Start')),
                ('receiving_dr_full_name', models.CharField(blank=True, max_length=150, verbose_name='Receiving Dr Full Name')),
                ('comments', models.TextField(blank=True, verbose_name='Comments')),
                ('needs_transfer', models.BooleanField(default=False, verbose_name='Needs Transfer')),
                ('international_redirect', models.BooleanField(default=False, verbose_name='International Redirect')),
                ('redirect_institution', models.CharField(blank=True, max_length=250, verbose_name='Redirect Institution')),
                ('specialty', models.CharField(blank=True, max_length=150, verbose_name='Specialty')),
                ('town', models.CharField(blank=True, max_length=150, verbose_name='Town')),
                ('country', models.CharField(blank=True, max_length=150, verbose_name='Country')),
                ('reason', models.TextField(blank=True, verbose_name='Reason')),
                ('clinic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rel_clinics', to='dispatch.clinic')),
                ('request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='med_assistance', to='dispatch.patientrequest')),
            ],
        ),
        migrations.CreateModel(
            name='LogisticAndSocialAssistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transport_required', models.BooleanField(default=False, help_text='Wether national or international transportation is required for this assistence', verbose_name='Transport Required')),
                ('transport_status', models.CharField(choices=[('US', 'Unsolved'), ('S', 'Solved')], default='US', max_length=2, verbose_name='Transport Status')),
                ('transport', models.CharField(blank=True, choices=[('NAT', 'National'), ('INT', 'International')], default='NAT', max_length=3, verbose_name='Transport')),
                ('pick_up_location', models.CharField(blank=True, help_text='Departing from: City, Country', max_length=200, verbose_name='Pick Up Location')),
                ('destination_location', models.CharField(blank=True, help_text='Departing from: City, Country', max_length=200, verbose_name='Pick Up Location')),
                ('transport_details', models.TextField(blank=True, verbose_name='Transport Details')),
                ('transport_rep_external', models.BooleanField(default=False, help_text='Is the transport representative external to the organization?', verbose_name='External Transport Representative')),
                ('transport_rep_external_details', models.TextField(blank=True, verbose_name='External Transport Representantive Details')),
                ('accommodation_required', models.BooleanField(default=False, help_text='Wether accommodation is required for this assistence', verbose_name='Accommodation Required')),
                ('accommodation_status', models.CharField(choices=[('US', 'Unsolved'), ('S', 'Solved')], default='US', max_length=2, verbose_name='Accommodation Status')),
                ('accommodation_details', models.TextField(blank=True, null=True, verbose_name='Accommodation Details')),
                ('accommodation_rep_external', models.BooleanField(default=False, help_text='Is the accommodation representative external to the organization?', verbose_name='External accommodation Representative')),
                ('accommodation_rep_external_details', models.TextField(blank=True, verbose_name='External Accommodation Representantive Details')),
                ('assistance_required', models.BooleanField(default=False, help_text='Wether assistance is required', verbose_name='Assistance Required')),
                ('assistance_status', models.CharField(choices=[('US', 'Unsolved'), ('S', 'Solved')], default='US', max_length=2, verbose_name='Assistance Status')),
                ('assistance_rep_external', models.BooleanField(default=False, help_text='Is the assistance representative external to the organization?', verbose_name='External Assistance Representative')),
                ('assistance_rep_external_details', models.TextField(blank=True, verbose_name='External Assistance Representantive Details')),
                ('request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='logsol_assistance', to='dispatch.patientrequest')),
            ],
        ),
        migrations.CreateModel(
            name='Companion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companion_name', models.CharField(blank=True, max_length=150, verbose_name='Companion Name')),
                ('companion_relationship', models.CharField(blank=True, max_length=150, verbose_name='Companion Relationship')),
                ('companion_phone_number', models.CharField(blank=True, help_text='Please include country prefix e.g. +40723000123', max_length=30, verbose_name='Companion Phone Number')),
                ('companion_other_details', models.TextField(blank=True, verbose_name='Companion Other Details')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companions', to='dispatch.patientrequest')),
            ],
        ),
    ]
