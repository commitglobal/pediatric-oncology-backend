from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _

EMAIL_TEMPLATE_CHOICES = [
    ("patient_request", _("Patient request form email")),
]


class EmailTemplate(models.Model):
    template = models.CharField(_("Template"), choices=EMAIL_TEMPLATE_CHOICES, max_length=254, unique=True)
    text_content = models.TextField(_("Text content"))
    html_content = RichTextField(_("HTML content"), blank=True)

    class Meta:
        verbose_name = _("Email template")
        verbose_name_plural = _("Email templates")

    def __str__(self):
        return self.template
