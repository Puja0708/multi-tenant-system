from __future__ import unicode_literals, absolute_import

from django import forms

from employees.apps import EmployeesConfig
from employees.models import Employee, EmployeeRoles


class CreateEmployeeForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    role = forms.IntegerField(required=False)
    team = forms.IntegerField(required=False)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=EmployeesConfig.GENDER_CHOICES)
    hire_date = forms.DateField(required=True)
    display_id = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.IntegerField(required=True)


class UpdateEmployeeForm(forms.Form):
    role = forms.IntegerField(required=False)
    team = forms.IntegerField(required=False)
    age = forms.IntegerField(required=False)
    is_active = forms.BooleanField(required=False)


class CreateEmployeeRoleForm(forms.Form):
    label = forms.CharField(required=True)

    class Meta:
        model = EmployeeRoles
        fields = '__all__'
