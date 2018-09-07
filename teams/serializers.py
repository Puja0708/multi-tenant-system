from __future__ import absolute_import, unicode_literals

from rest_framework import serializers

from teams.models import Teams


class TeamsSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Teams
        fields = '__all__'
