# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from teams.views import TeamsViewSet


urlpatterns = [
    url(r'^', TeamsViewSet.as_view({'post': 'create', 'get': 'list'})),
]
