from __future__ import unicode_literals, absolute_import

from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from tenant_schemas.utils import schema_context

from multi_tenant_system.helpers import get_schema_from_request
from teams.forms import CreateTeamForm
from teams.models import Teams
from teams.serializers import TeamsSerializer


class TeamsViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'teams.html'
    query_set = Teams.objects.all()
    serializer_class = TeamsSerializer

    def list(self, request, *args, **kwargs):
        form = CreateTeamForm()
        return render(request, 'teams.html', {'form': form})

    def create(self, request, *args, **kwargs):
        model_form = CreateTeamForm(request.POST)
        if model_form.is_valid():
            employee_data = model_form.cleaned_data
            schema_name = get_schema_from_request(request)
            import ipdb
            ipdb.set_trace()
            with schema_context(schema_name):
                serializer = self.get_serializer(data=employee_data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    raise Response(status=422)
            return HttpResponseRedirect('/')
        else:
            return Response({'errors': model_form.errors}, status=422)
