from __future__ import unicode_literals, absolute_import

from django import forms

from employees.models import Employee


class CreateEmployeeForm(forms.ModelForm):
    role = forms.CharField(null=True)
    team = forms.CharField(null=True)
    age = forms.IntegerField(null=True)
    first_name = forms.CharField(max_length=14, unique=True)
    last_name = forms.CharField(max_length=16)
    gender = forms.CharField(max_length=10)
    hire_date = forms.DateField()
    display_id = forms.CharField(unique=True, max_length=5)
    email = forms.CharField(max_length=50)
    phone_number = forms.IntegerField()

    class Meta:
        model = Employee
        fields = ('role', 'team', 'age', )