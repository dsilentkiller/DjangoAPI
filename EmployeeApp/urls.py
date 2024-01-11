"""DjangoAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from DjangoAPI.EmployeeApp.views import SaveFile, departmentApi
from django.contrib import admin
from django.urls import path
from django.conf.urls import url 
from EmployeeApp import views 
from django.conf.urls.static import static 

urlpatterns = [
    path('department/', views.departmentApi),
    url(r'^department/([0-9]+)$', views.departmentApi), 
    url(r'^employee/&', views.employeeApi),
    url(r'^employee/([0-9]+)$', views.employeeApi),
    url (r'^Employee/SaveFiles$', views.SaveFile),
   
] + static(settings.MEDIA_URL,documents_root=settings.MEDIA_ROOT)
