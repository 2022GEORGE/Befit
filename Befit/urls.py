"""Befit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from Befitapp.views import *
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^', index,name="index"),
    # url(r'^index/', index,name="index"),
    url(r'^login/', login,name="login"),
    url(r'^Registration/', Registration,name="Registration"),
    url(r'^Registrationaction/', Registrationaction,name="Registrationaction"),
    url(r'^medical/', medical,name="medical"),
    url(r'^medicalaction/', medicalaction,name="medicalaction"),
    url(r'^nutrition/', nutrition,name="nutrition"),
    url(r'^nutritionaction/', nutritionaction,name="nutritionaction"),
    url(r'^dietitian/', dietitian,name="dietitian"),
    url(r'^dietitianaction/', dietitianaction,name="dietitianaction"),
    url(r'^healthclub/', healthclub,name="healthclub"),
    url(r'^healthclubaction/', healthclubaction,name="healthclubaction"),
    url(r'^viewdiet/', viewdiet,name="viewdiet"),
    url(r'^viewdietaction/', viewdietaction,name="viewdietaction"),


    
    

]
