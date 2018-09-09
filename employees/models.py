from __future__ import unicode_literals

from django.db import models

from employees.apps import EmployeesConfig
from multi_tenant_system.utils import get_current_utc_timestamp, get_current_utc
from teams.models import Teams


class EmployeeRoles(models.Model):
    label = models.CharField(max_length=5)
    entry_timestamp = models.IntegerField(default=get_current_utc_timestamp)


class Employee(models.Model):
    REQUIRED_FIELDS = ('gender', 'age', 'email', 'phone_number')
    USERNAME_FIELD = 'first_name'
    is_anonymous = False
    is_authenticated = True

    role = models.ForeignKey(EmployeeRoles, models.DO_NOTHING, null=True)
    team = models.ForeignKey(Teams, models.DO_NOTHING, null=True)
    age = models.IntegerField(null=True)
    first_name = models.CharField(max_length=14, unique=True)
    last_name = models.CharField(max_length=16)
    gender = models.CharField(max_length=1, choices=EmployeesConfig.GENDER_CHOICES)
    hire_date = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    display_id = models.CharField(unique=True, max_length=5)
    email = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    entry_timestamp = models.IntegerField(default=get_current_utc_timestamp)

    class Meta:
        managed = True
        db_table = 'employees'

    def __str__(self):
        return str(self.first_name) + str(self.last_name)
