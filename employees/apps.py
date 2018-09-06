from __future__ import unicode_literals

from django.apps import AppConfig


class EmployeesConfig(AppConfig):
    name = 'employees'

    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female")
    )
