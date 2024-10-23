# Copyright 2024 Canonical Ltd.
# See LICENSE file for licensing details.

"""ACL views tests."""

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token

from acl.models import Acl


class AclViewTest(TestCase):
    """ACL views tests."""

    def setUp(self):
        """Create a new user and token for testing purposes."""
        self.user = User.objects.create_user('testuser', 'testuser@example.com', 'password')
        self.token = Token.objects.create(user=self.user)

    def test_create_acl(self):
        """Test creating an Access Control List (ACL) for a given account and zone."""
        response = self.client.post(
            reverse("acl", args=['test-account', 'test-zone']),
            HTTP_AUTHORIZATION=f'Token {self.token.key}',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Acl.objects.count(), 1)

    def test_delete_acl(self):
        """Test deleting an Access Control List (ACL) for a given account and zone."""
        Acl.objects.create(service_account='test-account', zone='test-zone')
        response = self.client.delete(
            reverse("acl", args=['test-account', 'test-zone']),
            HTTP_AUTHORIZATION=f'Token {self.token.key}',
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Acl.objects.filter(service_account='test-account', zone='test-zone').exists())

    def test_delete_acl_not_found(self):
        """Test trying to delete inexistant Access Control List (ACL) for a given account and zone."""
        response = self.client.delete(
            reverse("acl", args=['test-account', 'test-zone']),
            HTTP_AUTHORIZATION=f'Token {self.token.key}',
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_acl_exists(self):
        """Test checking existant Access Control List (ACL) for a given account and zone."""
        Acl.objects.create(service_account='test-account', zone='test-zone')
        response = self.client.get(
            reverse("acl", args=['test-account', 'test-zone']),
            HTTP_AUTHORIZATION=f'Token {self.token.key}',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'exists': True})

    def test_acl_not_exists(self):
        """Test checking unexistant Access Control List (ACL) for a given account and zone."""
        response = self.client.get(
            reverse("acl", args=['test-account', 'test-zone']),
            HTTP_AUTHORIZATION=f'Token {self.token.key}',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'exists': False})
