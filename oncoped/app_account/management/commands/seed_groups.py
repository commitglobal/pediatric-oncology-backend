from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

from app_account.models import DEFAULT_USER_GROUP


DEFAULT_USER_GROUP_PERMISSIONS = [
    "view_patientrequest",
    "add_patientrequest",
    "change_patientrequest",
    "delete_patientrequest"
]


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users_group, _ = Group.objects.get_or_create(name=DEFAULT_USER_GROUP)
        users_group.permissions.set(
            Permission.objects.filter(codename__in=DEFAULT_USER_GROUP_PERMISSIONS).values_list("id", flat=True)
        )
        self.stdout.write(
            self.style.SUCCESS(f"'{DEFAULT_USER_GROUP}' group has been created and appropriate permissions were assigned")
        )
