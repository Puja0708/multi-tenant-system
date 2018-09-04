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

    entry_timestamp = models.IntegerField(null=False)  # TODO : use mixins
    modified_timestamp = models.IntegerField(null=True)

    auto_create_schema = True


# class Client(TenantMixin):
#     name = models.CharField(max_length=100)
#     paid_until =  models.DateField()
#     on_trial = models.BooleanField()
#     created_on = models.DateField(auto_now_add=True)
#
#     # default true, schema will be automatically created and synced when it is saved
#     auto_create_schema = True
