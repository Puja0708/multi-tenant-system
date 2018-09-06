from __future__ import absolute_import, unicode_literals

from rest_framework import serializers

from companies.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Company
        fields = '__all__'
