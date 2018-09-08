from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from companies.forms import CreateCompanyForm
from companies.models import Company
from companies.serializers import CompanySerializer


class CompanyViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_detail.html'
    query_set = Company.objects.all()
    serializer_class = CompanySerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAdminUser,)  # since only admin user can view/ create companies

    def get(self, request):
        form = CreateCompanyForm()
        return render(request, 'profile_list.html', {'form': form})

    def post(self, request):
        model_form = CreateCompanyForm(request.POST)
        if model_form.is_valid():
            company_data = model_form.cleaned_data
            serializer = CompanySerializer(data=company_data)
            serializer.save()
            return HttpResponseRedirect('/')
        else:
            return Response({'errors': model_form.errors}, status=400)
