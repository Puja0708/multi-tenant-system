from __future__ import unicode_literals

from django.db import models
from safedelete.models import SafeDeleteModel
from tenant_schemas.models import TenantMixin



class Company(TenantMixin):

    name = models.CharField(max_length=1000, blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True, null=True)
    city = models.CharField(max_length=1000, blank=True, null=True)
    pincode = models.IntegerField(null=False)

    # entry_user = models.ForeignKey(null=False)  # TODO : populate using django auth
    # modified_user = models.ForeignKey(null=True)

    entry_timestamp = models.IntegerField(null=True)  # TODO : use mixins
    modified_timestamp = models.IntegerField(null=True)

    auto_create_schema = True
