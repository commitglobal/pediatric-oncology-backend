# Generated by Django 3.2.12 on 2022-03-12 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispatch', '0014_patientrequest_translator_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientrequest',
            name='known_complete_diagnostic',
            field=models.CharField(choices=[('1', 'Yes'), ('0', 'No')], default=0, max_length=2, verbose_name='Complete Diagnostic Known'),
        ),
    ]