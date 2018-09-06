# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import QueryDict
from rest_framework.generics import GenericAPIView

from mom_supply_chain.utils.dates import get_current_utc_timestamp


class TrackModificationDataMixins(GenericAPIView):

    def shove(self, payload, method, timestamp):
        if method == 'POST':
            payload['entry_timestamp'] = timestamp
        payload['modified_timestamp'] = timestamp

    def get_serializer(self, *args, **kwargs):
        def injector(elements, method, timestamp):
            for key, value in elements.items():
                if isinstance(value, list):
                    for val in value:
                        if isinstance(val, dict):
                            injector(val, method, timestamp)
                            self.shove(val, method, timestamp)
            self.shove(elements, method, timestamp)

        def inject(elements, method, timestamp):
            if isinstance(elements, list):
                for element in elements:
                    injector(element, method, timestamp)
            else:
                injector(elements, method, timestamp)

        if 'data' in kwargs and not isinstance(kwargs['data'], QueryDict):
            inject(kwargs['data'], self.request.method, get_current_utc_timestamp())
        elif 'data' in kwargs and isinstance(kwargs['data'], QueryDict):
            kwargs['data'] = kwargs['data'].dict()
            inject(kwargs['data'], self.request.method, get_current_utc_timestamp())
        return super().get_serializer(*args, **kwargs)


class EntryUserMixins(TrackModificationDataMixins):

    def shove(self, payload, method, timestamp):
        if method == 'POST':
            payload['entry_user'] = self.request.user.id
        payload['modified_user'] = self.request.user.id
        super().shove(payload, method, timestamp)


class EntryInternalUserMixins(TrackModificationDataMixins):

    def shove(self, payload, method, timestamp):
        if method == 'POST':
            payload['entry_internal_user'] = self.request.user.id
        payload['modified_internal_user'] = self.request.user.id
        super().shove(payload, method, timestamp)
