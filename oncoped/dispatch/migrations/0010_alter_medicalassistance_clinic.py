# Generated by Django 3.2.12 on 2022-03-08 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dispatch', '0009_auto_20220308_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalassistance',
            name='clinic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clinics', to='dispatch.clinic'),
        ),
    ]
