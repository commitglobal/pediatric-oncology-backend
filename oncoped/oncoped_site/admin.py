from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import EmailTemplate


@admin.register(EmailTemplate)
class AdminEmailTemplate(admin.ModelAdmin):
    class Media:
        js = ('ckeditor.js',)