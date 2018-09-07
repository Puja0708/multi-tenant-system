"""multi_tenant_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.contrib.auth import views as auth_views

from companies.views import CompanyViewSet

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/', CompanyViewSet.as_view({'get': 'get', 'post': 'post'})),
    # url('rest-auth/', include('rest_auth.urls'))
    # url(r'^accounts/login/$', auth_views.login),
    # url( r'^login/$', auth_views.LoginView.as_view(template_name="login.html")),
    # url( r'^logout/$', auth_views.LoginView.as_view(template_name="logout.html")),
    # url(r'rest-auth/', include('rest_auth.urls'))
]
