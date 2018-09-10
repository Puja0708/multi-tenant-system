from __future__ import unicode_literals, absolute_import

from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.viewsets import ModelViewSet
from tenant_schemas.utils import schema_context

from multi_tenant_system.helpers import get_schema_from_request
from teams.forms import CreateTeamForm
from teams.models import Teams
from teams.serializers import TeamsSerializer


class TeamsViewSet(ModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'teams.html'
    query_set = Teams.objects.all()
    serializer_class = TeamsSerializer

    def list(self, request, *args, **kwargs):
        form = CreateTeamForm()
        return render(request, 'teams.html', {'form': form})

    def create(self, request, *args, **kwargs):
        """
        View to be used by companies to create teams.
        Employees can join these teams afterwards.
        TODO : authenticate company
        """
        model_form = CreateTeamForm(request.POST)
        schema_name = get_schema_from_request(request)
        with schema_context(schema_name):
            if model_form.is_valid():
                model_form.save()
                return render(request, 'success.html', {'error': model_form.cleaned_data})
            else:
                return render(request, 'errors.html', {'error': model_form.errors})
