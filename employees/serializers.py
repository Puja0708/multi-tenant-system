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


class EmployeeViewUpdateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(read_only=False, required=False)
    last_name = serializers.CharField(read_only=False, required=False)
    team = serializers.IntegerField(required=False)
    age = serializers.IntegerField(required=False)

    class Meta(object):
        model = Employee
        fields = '__all__'
