# Copyright 2024 Canonical Ltd.
# See LICENSE file for licensing details.

"""ACL serializers."""

from rest_framework import serializers

from .models import Acl


class AclSerializer(serializers.ModelSerializer):
    """ACL serializer."""

    class Meta:
        """Meta of the ACL serializer."""
        model = Acl
        fields = ['service_account', 'zone']
