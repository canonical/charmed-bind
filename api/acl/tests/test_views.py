from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from acl.models import Acl
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class AclViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'testuser@example.com', 'password')
        self.token = Token.objects.create(user=self.user)

    def test_create_acl(self):
        response = self.client.post(
            reverse("acl", args=['test-account', 'test-zone']),
            HTTP_AUTHORIZATION=f'Token {self.token.key}',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Acl.objects.count(), 1)

    def test_delete_acl(self):
        Acl.objects.create(service_account='test-account', zone='test-zone')
        response = self.client.delete(
            reverse("acl", args=['test-account', 'test-zone']),
            HTTP_AUTHORIZATION=f'Token {self.token.key}',
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Acl.objects.filter(service_account='test-account', zone='test-zone').exists())

    def test_delete_acl_not_found(self):
        response = self.client.delete(
            reverse("acl", args=['test-account', 'test-zone']),
            HTTP_AUTHORIZATION=f'Token {self.token.key}',
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_acl_exists(self):
        Acl.objects.create(service_account='test-account', zone='test-zone')
        response = self.client.get(
            reverse("acl", args=['test-account', 'test-zone']),
            HTTP_AUTHORIZATION=f'Token {self.token.key}',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'exists': True})

    def test_acl_not_exists(self):
        response = self.client.get(
            reverse("acl", args=['test-account', 'test-zone']),
            HTTP_AUTHORIZATION=f'Token {self.token.key}',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'exists': False})
