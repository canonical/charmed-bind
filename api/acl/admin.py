# Copyright 2024 Canonical Ltd.
# See LICENSE file for licensing details.

"""Admin module registration."""

from django.contrib import admin

from .models import Acl

admin.site.register(Acl)
