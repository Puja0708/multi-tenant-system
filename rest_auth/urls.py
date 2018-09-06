from __future__ import unicode_literals, absolute_import

from django.conf.urls import url
from django.contrib import admin
from django.urls import include

from companies.views import CompanyViewSet

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^test/', CompanyViewSet.as_view({'get': 'get', 'post': 'post'})),
    # url('rest-auth/', include('rest_auth.urls'))
]
