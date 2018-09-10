from __future__ import unicode_literals, absolute_import

from django import forms

from employees.apps import EmployeesConfig
from employees.models import Employee, EmployeeRoles


class EmployeeForm(forms.ModelForm):
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

    class Meta:
        model = Employee
        fields = '__all__'


class CreateEmployeeRoleForm(forms.ModelForm):
    label = forms.CharField(required=True)

    class Meta:
        model = EmployeeRoles
        fields = '__all__'
