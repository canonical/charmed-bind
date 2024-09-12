from django.core.management.base import BaseCommand
from acl.models import Acl


class Command(BaseCommand):
    help = 'Create a new ACL'

    def add_arguments(self, parser):
        parser.add_argument('service_account', help='Service account')
        parser.add_argument('zone', help='Zone')

    def handle(self, *args, **options):
        Acl.objects.create(service_account=options['service_account'], zone=options['zone'])
        self.stdout.write('ACL created successfully')
