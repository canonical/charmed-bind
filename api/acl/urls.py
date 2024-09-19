from django.urls import path
from .views import AclView

urlpatterns = [
    path('<str:service_account>/<str:zone>/', AclView.as_view(), name='acl'),
]
