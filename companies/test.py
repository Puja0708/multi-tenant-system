from __future__ import unicode_literals, absolute_import

from django.test import TestCase
from companies.models import Company


class CompanyTests(TestCase):
    def setUp(self):
        Company.objects.create(domain_url='example.com',
                schema_name='public',
                name='test name',
                address='test address',
                city='blr')
        Company.objects.create(domain_url='tenant1.example.com',
                               schema_name='tenant1',
                               name='test name',
                               address='test address',
                               city='blr')

    def test_public_tenant_created(self):
        public_tenant = Company.objects.get(schema_name='public')
        self.assertCountEqual(public_tenant, 1)


    def test_other_tenant_created(self):
        tenant = Company.objects.get(schema_name='tenant1')
        self.assertCountEqual(tenant, 1)
