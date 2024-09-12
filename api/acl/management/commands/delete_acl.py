from django.core.management.base import BaseCommand
from acl.models import Acl


class Command(BaseCommand):
    help = 'Delete an ACL'

    def add_arguments(self, parser):
        parser.add_argument('service_account', help='Service account')
        parser.add_argument('zone', help='Zone')

    def handle(self, *args, **options):
        acl = Acl.objects.filter(service_account=options['service_account'], zone=options['zone']).first()
        if acl:
            acl.delete()
            self.stdout.write('ACL deleted successfully')
        else:
            self.stdout.write('ACL does not exist')
