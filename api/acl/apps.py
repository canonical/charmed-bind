# Copyright 2024 Canonical Ltd.
# See LICENSE file for licensing details.

"""Main config class of the ACL module."""

from django.apps import AppConfig


class AclConfig(AppConfig):
    """Main config class of the ACL module."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'acl'
