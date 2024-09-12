from django.test import TestCase
from django.core.management import call_command
from io import StringIO
from acl.models import Acl


class CreateAclCommandTest(TestCase):
    def test_create_acl(self):
        call_command('create_acl', 'test-account', 'test-zone')
        acl = Acl.objects.get(service_account='test-account', zone='test-zone')
        self.assertEqual(acl.service_account, 'test-account')
        self.assertEqual(acl.zone, 'test-zone')


class CheckAclCommandTest(TestCase):
    def test_check_acl_exists(self):
        Acl.objects.create(service_account='test-account', zone='test-zone')
        output = StringIO()
        call_command('check_acl', 'test-account', 'test-zone', stdout=output)
        self.assertEqual(output.getvalue().strip(), 'ACL exists')

    def test_check_acl_does_not_exist(self):
        output = StringIO()
        call_command('check_acl', 'test-account', 'test-zone', stdout=output)
        self.assertEqual(output.getvalue().strip(), 'ACL does not exist')


class DeleteAclCommandTest(TestCase):
    def test_delete_acl(self):
        Acl.objects.create(service_account='test-account', zone='test-zone')
        call_command('delete_acl', 'test-account', 'test-zone')
        self.assertFalse(Acl.objects.filter(service_account='test-account', zone='test-zone').exists())

    def test_delete_acl_does_not_exist(self):
        output = StringIO()
        call_command('delete_acl', 'test-account', 'test-zone', stdout=output)
        self.assertEqual(output.getvalue().strip(), 'ACL does not exist')


class ListAclsCommandTest(TestCase):
    def test_list_acls(self):
        Acl.objects.create(service_account='test-account-1', zone='test-zone-1')
        Acl.objects.create(service_account='test-account-2', zone='test-zone-2')
        output = StringIO()
        call_command('list_acl', stdout=output)
        self.assertIn('test-account-1 - test-zone-1', output.getvalue())
        self.assertIn('test-account-2 - test-zone-2', output.getvalue())
