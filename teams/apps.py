from __future__ import unicode_literals

from django.apps import AppConfig


class TeamsConfig(AppConfig):
    name = 'teams'

    DEFAULT_MAX_PLAYERS_ALLOWED = 10
