from rest_framework import serializers
from .models import Acl


class AclSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acl
        fields = ['service_account', 'zone']
