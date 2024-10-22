# Copyright 2024 Canonical Ltd.
# See LICENSE file for licensing details.

"""ACL serializer tests."""

from django.test import TestCase

from acl.models import Acl
from acl.serializers import AclSerializer


class AclSerializerTest(TestCase):
    """ACL Serializer tests."""
    def test_serialize_acl(self):
        """Test serializing ACL."""
        acl = Acl(service_account='test-account', zone='test-zone')
        serializer = AclSerializer(acl)
        self.assertEqual(serializer.data, {
            'service_account': 'test-account',
            'zone': 'test-zone'
        })

    def test_deserialize_acl(self):
        """Test deserializing ACL."""
        data = {
            'service_account': 'test-account',
            'zone': 'test-zone'
        }
        serializer = AclSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        acl = serializer.save()
        self.assertEqual(acl.service_account, 'test-account')
        self.assertEqual(acl.zone, 'test-zone')
