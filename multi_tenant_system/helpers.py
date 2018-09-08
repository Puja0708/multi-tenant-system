from __future__ import unicode_literals, absolute_import

from tenant_schemas.utils import get_public_schema_name


def get_schema_from_request(request):
    return request.META.get('HTTP_X_DTS_SCHEMA', get_public_schema_name())  # TODO : check what it returns for public schema
