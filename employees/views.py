from __future__ import unicode_literals, absolute_import

from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.viewsets import ModelViewSet
from tenant_schemas.utils import schema_context

from employees.forms import EmployeeForm, CreateEmployeeRoleForm
from employees.models import Employee, EmployeeRoles
from employees.serializers import EmployeeViewSerializer, EmployeeRoleSerializer, EmployeeViewUpdateSerializer
from multi_tenant_system.helpers import get_schema_from_request


class EmployeeRoleViewSet(ModelViewSet):  # not giving the delete option right now
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
        schema_name = get_schema_from_request(request)
        with schema_context(schema_name):
            if model_form.is_valid():
                model_form.save()
                return render(request, 'success.html', {'data': model_form.cleaned_data})
            else:
                return render(request, 'errors.html', {'error': model_form.errors})


class EmployeeViewSet(ModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'employee.html'
    queryset = Employee.objects.all()
    form_class = EmployeeForm

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'PUT':
            return EmployeeViewUpdateSerializer(data=self.request.data)
        return EmployeeViewSerializer(data=self.request.data)

    def list(self, request, *args, **kwargs):
        form = EmployeeForm()
        return render(request, 'employee.html', {'form': form})

    def create(self, request, *args, **kwargs):
        """
        View to be used (by companies) to create an employee
        TODO : authenticate company
        """
        model_form = EmployeeForm(request.data)
        schema_name = get_schema_from_request(request)
        with schema_context(schema_name):
            if model_form.is_valid():
                model_form.save()
                return render(request, 'success.html', {'data': model_form.cleaned_data})
            else:
                return render(request, 'errors.html', {'errors': model_form.errors})


    def update(self, request, *args, **kwargs):
        """
        View to be used by Employee (or company) to edit employee information, like role, team etc
        TODO : authenticate company/employee
        """
        model_form = EmployeeForm(request.data)
        schema_name = get_schema_from_request(request)
        with schema_context(schema_name):
            if model_form.is_valid():
                model_form.save()
                return render(request, 'success.html', {'data': model_form.cleaned_data})
            else:
                return render(request, 'errors.html', {'error': model_form.errors})
