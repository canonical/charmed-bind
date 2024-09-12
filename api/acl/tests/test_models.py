from django.test import TestCase
from acl.models import Acl


class AclModelTest(TestCase):
    def test_create_acl(self):
        acl = Acl(service_account='test-account', zone='test-zone')
        acl.save()
        self.assertEqual(Acl.objects.count(), 1)
