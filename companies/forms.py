from __future__ import unicode_literals, absolute_import

from django import forms
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from tenant_schemas.utils import schema_exists


class CreateCompanyForm(forms.Form):
    schema_name = forms.CharField(label='Your name', max_length=100)
    domain_url = forms.CharField(label='URL', max_length=100)
    name = forms.CharField(label='tenant name', max_length=50)
    address = forms.CharField(label='address', max_length=1000)
    city = forms.CharField(label='city')
    pincode = forms.IntegerField()

    def clean_schema_name(self):
        schema_name = self.cleaned_data["schema_name"]
        schema_name = slugify(schema_name).replace("-", "")

        if schema_exists(schema_name):
            raise ValidationError("A schema with this name already exists in the database")
        else:
            return schema_name
