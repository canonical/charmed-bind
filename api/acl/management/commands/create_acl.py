# Copyright 2024 Canonical Ltd.
# See LICENSE file for licensing details.

"""Command that creates a new ACL."""

from django.core.management.base import BaseCommand

from acl.models import Acl


class Command(BaseCommand):
    """Command that creates a new ACL."""
    help = 'Create a new ACL'

    def add_arguments(self, parser):
        """Parse Arguments."""
        parser.add_argument('service_account', help='Service account')
        parser.add_argument('zone', help='Zone')

    def handle(self, *args, **options):
        """Execute command."""
        Acl.objects.create(service_account=options['service_account'], zone=options['zone'])
        self.stdout.write('ACL created successfully')
