from __future__ import unicode_literals, absolute_import

from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from employees.forms import CreateEmployeeForm, CreateEmployeeRoleForm, UpdateEmployeeForm
from employees.models import Employee, EmployeeRoles
from employees.serializers import EmployeeViewSerializer, EmployeeRoleSerializer, EmployeeViewUpdateSerializer
from multi_tenant_system.helpers import get_schema_from_request
from tenant_schemas.utils import schema_context


class EmployeeRoleViewSet(ListModelMixin, GenericViewSet):  # not giving the delete option right now
    queryset = EmployeeRoles.objects.all()
    serializer_class = EmployeeRoleSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'employee_roles.html'

    def create(self, request, *args, **kwargs):
        """
        View to be used by companies to create employee roles
        TODO : authenticate company
        """
        model_form = CreateEmployeeRoleForm(request.POST)
        if model_form.is_valid():
            employee_data = model_form.cleaned_data
            schema_name = get_schema_from_request(request)
            with schema_context(schema_name):
                serializer = self.get_serializer(data=employee_data)
                if serializer.is_valid():  # the form has done its bit of validation. Doing it here again because of DRF constraints
                    serializer.save()
            return HttpResponseRedirect('/')
        else:
            return Response({'errors': model_form.errors}, status=400)


class EmployeeViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'employee.html'
    queryset = Employee.objects.all()
    serializer_class = EmployeeRoleSerializer


    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'PUT':
            return EmployeeViewUpdateSerializer(data=self.request.POST)
        return EmployeeViewSerializer(data=self.request.POST)

    def list(self, request, *args, **kwargs):
        form = CreateEmployeeForm()
        return render(request, 'employee.html', {'form': form})

    def create(self, request, *args, **kwargs):
        """
        View to be used (by companies) to create an employee
        TODO : authenticate company
        """
        model_form = CreateEmployeeForm(request.POST)
        if model_form.is_valid():
            employee_data = model_form.cleaned_data
            schema_name = get_schema_from_request(request)
            with schema_context(schema_name):
                serializer = self.get_serializer(data=employee_data)
                if serializer.is_valid(): # the form has done its bit of validation. Doing it here again because of DRF constraints
                    serializer.save()
                else:
                    return render(request, 'errors.html', {'errors': serializer.errors})
            return HttpResponseRedirect('/')
        else:
            return render(request, 'errors.html', {'errors': model_form.errors})


    def update(self, request, *args, **kwargs):
        """
        View to be used by Employee (or company) to edit employee information, like role, team etc
        TODO : authenticate company/employee
        """
        model_form = UpdateEmployeeForm(request.POST)
        if model_form.is_valid():
            employee_data = model_form.cleaned_data
            schema_name = get_schema_from_request(request)
            with schema_context(schema_name):
                serializer = self.get_serializer(data=employee_data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                else:
                    return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            return HttpResponseRedirect('/')
        else:
            return Response({'errors': model_form.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
