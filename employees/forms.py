from __future__ import unicode_literals, absolute_import

from django import forms

from employees.models import Employee, EmployeeRoles


class CreateEmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('role', 'team', 'age', )


class UpdateEmployeeForm(forms.ModelForm):
    role = forms.IntegerField(required=False)
    team = forms.IntegerField(required=False)
    age = forms.IntegerField(required=False)
    is_active = forms.BooleanField(required=False)

    class Meta:
        model = Employee
        fields = ('role', 'team', 'age', )


class CreateEmployeeRoleForm(forms.ModelForm):

    class Meta:
        model = EmployeeRoles
        fields = '__all__'
