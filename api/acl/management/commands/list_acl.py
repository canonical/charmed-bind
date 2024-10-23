# Copyright 2024 Canonical Ltd.
# See LICENSE file for licensing details.

"""Command that lists all ACLs."""

from django.core.management.base import BaseCommand

from acl.models import Acl


class Command(BaseCommand):
    """Command that lists all ACLs."""
    help = 'List all ACLs'

    def handle(self, *args, **options):
        """Execute the command."""
        acls = Acl.objects.all()
        for acl in acls:
            self.stdout.write(f'{acl.service_account} - {acl.zone}')
