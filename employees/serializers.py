from __future__ import unicode_literals, absolute_import

from rest_framework import serializers

from employees.models import EmployeeRoles, Employee


class EmployeeRoleSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = EmployeeRoles
        fields = '__all__'


class EmployeeViewSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Employee
        fields = '__all__'
