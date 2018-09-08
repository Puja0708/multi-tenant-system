from __future__ import unicode_literals, absolute_import

from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from employees.forms import CreateEmployeeForm
from employees.models import Employee, EmployeeRoles
from employees.serializers import EmployeeViewSerializer, EmployeeRoleSerializer, EmployeeViewUpdateSerializer
from multi_tenant_system.helpers import get_schema_from_request
from tenant_schemas.utils import schema_context


class EmployeeRoleViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    query_set = EmployeeRoles.objects.all()
    serializer_class = EmployeeRoleSerializer
    # TODO : make employee roles for tenant

class EmployeeViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_detail.html'
    query_set = Employee.objects.all()

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'PUT':
            return EmployeeViewUpdateSerializer()
        return EmployeeViewSerializer()

    def list(self, request, *args, **kwargs):
        form = CreateEmployeeForm()
        return render(request, 'profile_list.html', {'form': form})

    def create(self, request, *args, **kwargs):
        model_form = CreateEmployeeForm(request.POST)
        if model_form.is_valid():
            employee_data = model_form.cleaned_data
            schema_name = get_schema_from_request(request)
            with schema_context(schema_name):
                serializer = self.get_serializer(data=employee_data)
                serializer.save()
            return HttpResponseRedirect('/')
        else:
            return Response({'errors': model_form.errors}, status=400)
