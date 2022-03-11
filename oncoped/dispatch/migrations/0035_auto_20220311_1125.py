# Generated by Django 3.2.12 on 2022-03-11 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispatch', '0034_auto_20220311_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='logisticandsocialassistance',
            name='accommodation_status',
            field=models.CharField(default='US', max_length=2, verbose_name='Accommodation Status'),
        ),
        migrations.AddField(
            model_name='logisticandsocialassistance',
            name='assistance_rep_external',
            field=models.BooleanField(default=False, help_text='Is the assistance representative external to the organization?', verbose_name='External Assistance Representative'),
        ),
        migrations.AddField(
            model_name='logisticandsocialassistance',
            name='assistance_rep_external_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='logisticandsocialassistance',
            name='assistance_required',
            field=models.BooleanField(default=False, help_text='Wether assistance is required', verbose_name='Assistance Required'),
        ),
        migrations.AddField(
            model_name='logisticandsocialassistance',
            name='assistance_status',
            field=models.CharField(default='US', max_length=2, verbose_name='Assistance Status'),
        ),
        migrations.AddField(
            model_name='logisticandsocialassistance',
            name='transport_status',
            field=models.CharField(default='US', max_length=2, verbose_name='Transport Status'),
        ),
    ]
