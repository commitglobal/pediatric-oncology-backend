# Generated by Django 3.2.12 on 2022-03-10 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dispatch', '0024_auto_20220309_2326'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='patientrequest',
            unique_together={('first_name', 'last_name', 'birth_date')},
        ),
        migrations.RemoveField(
            model_name='patientrequest',
            name='age',
        ),
    ]