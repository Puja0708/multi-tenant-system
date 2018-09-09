from __future__ import unicode_literals, absolute_import

from django.test import TestCase
from companies.models import Company
from employees.models import Employee, EmployeeRoles
from tenant_schemas.utils import schema_context

def create_tenants():
    if not Company.objects.all():
        Company.objects.create(domain_url='example.com',
                               schema_name='public',
                               name='test name',
                               address='test address',
                               city='blr',
                               pincode=1234)
        Company.objects.create(domain_url='tenant1.example.com',
                               schema_name='tenant1',
                               name='test name',
                               address='test address',
                               city='blr',
                               pincode=1234)


class EmployeeRolesTests(TestCase):
    def setUp(self):
        create_tenants()
        with schema_context('public'):
            EmployeeRoles.objects.create(label='senior')

        with schema_context('tenant1'):
            EmployeeRoles.objects.create(label='intern')

    def test_employee_roles(self):
        with schema_context('public'):
            public_emp_roles = EmployeeRoles.objects.all()
        with schema_context('tenant1'):
            other_tenant_employee_roles = EmployeeRoles.objects.all()

        self.assertCountEqual(public_emp_roles, 1)
        self.assertCountEqual(other_tenant_employee_roles, 1)



class EmployeeTests(TestCase):
    def setUp(self):
        create_tenants()  # TODO : use factories
        with schema_context('public'):
            Employee.objects.create(first_name='test',
                                    gender='F',
                                    age=1,
                                    email='adb.dsk@mdn',
                                    phone_number=23682492)
        with schema_context('tenant1'):
            Employee.objects.create(first_name='test',
                                    gender='F',
                                    age=1,
                                    email='adb.dsk@mdn',
                                    phone_number=236823672)

    def test_employee_roles(self):
        with schema_context('public'):
            public_employees = Employee.objects.all()
        with schema_context('tenant1'):
            other_tenant_employees = Employee.objects.all()

        self.assertCountEqual(public_employees, 1)
        self.assertCountEqual(other_tenant_employees, 1)
