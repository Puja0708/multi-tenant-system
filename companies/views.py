from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponseRedirect

from companies.forms import CreateCompanyForm
from companies.models import Company
from companies.serializers import CompanySerializer

from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, ListModelMixin


class CompanyDetail(CreateModelMixin, ListModelMixin,  GenericViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_detail.html'
    query_set = Company.objects.all()
    # serializer_class = CompanySerializer

    def get(self, request):
        form = CreateCompanyForm()
        return render(request, 'profile_list.html', {'form': form})


    def post(self, request):
        model_form = CreateCompanyForm(request.POST)
        if model_form.is_valid():
            company_data = model_form.cleaned_data
            import ipdb
            ipdb.set_trace()
            serializer = CompanySerializer(data=company_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return HttpResponseRedirect('/')
        else:
            return Response({'errors': model_form.errors}, status=400)
