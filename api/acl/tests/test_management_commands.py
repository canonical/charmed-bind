# Copyright 2024 Canonical Ltd.
# See LICENSE file for licensing details.

"""TestManagement commands."""

from io import StringIO

from django.core.management import call_command
from django.test import TestCase

from acl.models import Acl


class CreateAclCommandTest(TestCase):
    """ACL commands tests."""

    def test_create_acl(self):
        """Test the create ACL command."""
        call_command('create_acl', 'test-account', 'test-zone')
        acl = Acl.objects.get(service_account='test-account', zone='test-zone')
        self.assertEqual(acl.service_account, 'test-account')
        self.assertEqual(acl.zone, 'test-zone')


class CheckAclCommandTest(TestCase):
    """Test the check ACL command."""

    def test_check_acl_exists(self):
        """Test the check ACL command."""
        Acl.objects.create(service_account='test-account', zone='test-zone')
        output = StringIO()
        call_command('check_acl', 'test-account', 'test-zone', stdout=output)
        self.assertEqual(output.getvalue().strip(), 'ACL exists')

    def test_check_acl_does_not_exist(self):
        """Test the check ACL command with it non-existing."""
        output = StringIO()
        call_command('check_acl', 'test-account', 'test-zone', stdout=output)
        self.assertEqual(output.getvalue().strip(), 'ACL does not exist')


class DeleteAclCommandTest(TestCase):
    """Test the delete ACL command."""

    def test_delete_acl(self):
        """Test the delete ACL command."""
        Acl.objects.create(service_account='test-account', zone='test-zone')
        call_command('delete_acl', 'test-account', 'test-zone')
        self.assertFalse(Acl.objects.filter(service_account='test-account', zone='test-zone').exists())

    def test_delete_acl_does_not_exist(self):
        """Test the delete ACL command with it non-existing."""
        output = StringIO()
        call_command('delete_acl', 'test-account', 'test-zone', stdout=output)
        self.assertEqual(output.getvalue().strip(), 'ACL does not exist')


class ListAclsCommandTest(TestCase):
    """Test the list ACLs command."""

    def test_list_acls(self):
        """Test the list ACLs command."""
        Acl.objects.create(service_account='test-account-1', zone='test-zone-1')
        Acl.objects.create(service_account='test-account-2', zone='test-zone-2')
        output = StringIO()
        call_command('list_acl', stdout=output)
        self.assertIn('test-account-1 - test-zone-1', output.getvalue())
        self.assertIn('test-account-2 - test-zone-2', output.getvalue())
