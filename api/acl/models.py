from django.db import models
from django.db.models.constraints import UniqueConstraint


class Acl(models.Model):
    service_account = models.TextField()
    zone = models.TextField()

    def __str__(self):
        return f"{self.service_account} - {self.zone}"

    class Meta:
        constraints = [
            UniqueConstraint('service_account', 'zone', name="unique_acl")
        ]
        verbose_name = 'Access Control List'
        verbose_name_plural = 'Access Control Lists'
