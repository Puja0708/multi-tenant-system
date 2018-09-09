from __future__ import unicode_literals

from django.db import models
from safedelete.models import SafeDeleteModel
from tenant_schemas.models import TenantMixin

from multi_tenant_system.utils import get_current_utc_timestamp


class Company(TenantMixin):

    name = models.CharField(max_length=1000, blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True, null=True)
    city = models.CharField(max_length=1000, blank=True, null=True)
    pincode = models.IntegerField(null=False)

    entry_timestamp = models.IntegerField(default=get_current_utc_timestamp)  # TODO : use mixins
    modified_timestamp = models.IntegerField(null=True)

    auto_create_schema = True

    class Meta:
        managed = True
        db_table = 'companies'
