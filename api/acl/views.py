from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Acl
from .serializers import AclSerializer


class AclView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, service_account, zone):
        acl = Acl.objects.filter(service_account=service_account, zone=zone).first()
        if acl:
            return Response({'exists': True})
        return Response({'exists': False})

    def post(self, request, service_account, zone):
        serializer = AclSerializer(data={'service_account': service_account, 'zone': zone})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, service_account, zone):
        acl = Acl.objects.filter(service_account=service_account, zone=zone).first()
        if acl:
            acl.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
