from django.core.management.base import BaseCommand
from acl.models import Acl


class Command(BaseCommand):
    help = 'List all ACLs'

    def handle(self, *args, **options):
        acls = Acl.objects.all()
        for acl in acls:
            self.stdout.write(f'{acl.service_account} - {acl.zone}')
