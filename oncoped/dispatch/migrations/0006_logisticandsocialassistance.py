# Generated by Django 3.2.12 on 2022-03-08 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dispatch', '0005_auto_20220308_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogisticAndSocialAssistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick_up_location', models.CharField(blank=True, max_length=150, null=True, verbose_name='Pick Up Location')),
                ('contact_person', models.CharField(blank=True, max_length=150, null=True, verbose_name='Contact Person')),
                ('transport_required', models.BooleanField(default=True, help_text='Wether national or international transportation is required for this assistence', verbose_name='Transport Required')),
                ('transport', models.CharField(blank=True, choices=[('NAT', 'National'), ('INT', 'International')], default='NAT', max_length=3, null=True, verbose_name='Transport')),
                ('transport_details', models.TextField(blank=True, help_text='Details: contact person / problem owner, phone number, other details.', null=True, verbose_name='Transport Details')),
                ('accommodation_required', models.BooleanField(default=True, help_text='Wether accommodation is required for this assistence', verbose_name='Accommodation Required')),
                ('accommodation_details', models.TextField(blank=True, help_text='Details: contact person / problem owner, phone number, other details.', null=True, verbose_name='Accommodation Details')),
                ('destination_asisting_entity_details', models.TextField(blank=True, help_text='Info & contact details of the Organization/Person providing social assitance at destination', null=True, verbose_name='Destination Assisting Entity Details')),
                ('request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dispatch.patientrequest')),
            ],
        ),
    ]
