# Copyright 2024 Canonical Ltd.
# See LICENSE file for licensing details.

"""ACL model."""

from django.db import models
from django.db.models.constraints import UniqueConstraint


class Acl(models.Model):
    """ACL model."""
    service_account = models.TextField()
    zone = models.TextField()

    def __str__(self):
        """Return string rep of the ACL model."""
        return f"{self.service_account} - {self.zone}"

    class Meta:
        """Meta of the ACL model."""
        constraints = [
            UniqueConstraint('service_account', 'zone', name="unique_acl")
        ]
        verbose_name = 'Access Control List'
        verbose_name_plural = 'Access Control Lists'
