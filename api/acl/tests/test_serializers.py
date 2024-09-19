from django.test import TestCase
from acl.models import Acl
from acl.serializers import AclSerializer


class AclSerializerTest(TestCase):
    def test_serialize_acl(self):
        acl = Acl(service_account='test-account', zone='test-zone')
        serializer = AclSerializer(acl)
        self.assertEqual(serializer.data, {
            'service_account': 'test-account',
            'zone': 'test-zone'
        })

    def test_deserialize_acl(self):
        data = {
            'service_account': 'test-account',
            'zone': 'test-zone'
        }
        serializer = AclSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        acl = serializer.save()
        self.assertEqual(acl.service_account, 'test-account')
        self.assertEqual(acl.zone, 'test-zone')
