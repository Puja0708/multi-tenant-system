from __future__ import unicode_literals

from django.db import models

from multi_tenant_system.utils import get_current_utc_timestamp
from teams.apps import TeamsConfig


class Teams(models.Model):
    name = models.CharField(null=False, max_length=5)
    entry_timestamp = models.IntegerField(default=get_current_utc_timestamp)
    is_active = models.BooleanField(default=True)
    max_members = models.IntegerField(default=TeamsConfig.DEFAULT_MAX_PLAYERS_ALLOWED)

    class Meta:
        managed = True