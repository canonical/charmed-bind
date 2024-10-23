# Copyright 2024 Canonical Ltd.
# See LICENSE file for licensing details.

"""ACL views."""

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Acl
from .serializers import AclSerializer


class AclView(APIView):
    """ACL views."""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, service_account, zone):
        """Return an HTTP response indicating whether an ACL for the specified service account and zone exists.

        Args:
            request: The current request.
            service_account (str): The ID of the service account.
            zone (str): The name of the zone.

        Returns:
            Response: A 200 OK response with a JSON body containing 'exists' as either True or False, based on whether an ACL exists for the specified service account and zone.
        """
        acl = Acl.objects.filter(service_account=service_account, zone=zone).first()
        if acl:
            return Response({'exists': True})
        return Response({'exists': False})

    def post(self, request, service_account, zone):
        """Create an access control list (ACL) for a specified service account and zone.

        This method creates a new ACL entry in the database, specifying the service account and zone.

        Args:
            request (HttpRequest): The incoming HTTP request object.
            service_account (str): The ID of the service account to be created.
            zone (str): The zone for which the ACL is being created.

        Returns:
            Response: A 201 Created response if the request is valid, otherwise a 400 Bad Request response with the error details.

        Raises:
            ValidationError: If the serializer's validation fails.
        """
        serializer = AclSerializer(data={'service_account': service_account, 'zone': zone})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, service_account, zone):
        """Delete an access control list (ACL) for a given service account and zone.

        Args:
            request: The HTTP request object.
            service_account: The ID of the service account to delete the ACL for.
            zone: The ID of the zone associated with the ACL to delete.

        Returns:
            A response indicating that the operation was successful (204 No Content).
            A 404 Not Found response if the ACL does not exist or is inaccessible.

        Raises:
            ValueError: If the request contains invalid data or if the service account or zone are missing.
        """
        acl = Acl.objects.filter(service_account=service_account, zone=zone).first()
        if acl:
            acl.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
