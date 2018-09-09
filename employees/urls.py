# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from employees.views import EmployeeViewSet, EmployeeRoleViewSet

urlpatterns = [
    url(r'^', EmployeeViewSet.as_view({'post': 'create', 'get': 'list'})),
    url(r'^roles/', EmployeeRoleViewSet.as_view({'post': 'create', 'get': 'list', 'put': 'update', 'patch': 'update'})),
]
