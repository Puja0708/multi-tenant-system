from __future__ import unicode_literals, absolute_import

from tenant_schemas.utils import get_public_schema_name


def get_schema_from_request(request):
<<<<<<< HEAD
    return 't1'
=======
>>>>>>> fc7a5c24747754e98cbfd4fb7b8a24e2cafade12
    return request.META.get('HTTP_X_DTS_SCHEMA', get_public_schema_name())

