"""
URL configuration for covid_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from covid_data import views
from covid_data.views import covid_data, covid_data_post

urlpatterns = [
    path("admin/", admin.site.urls),
    path('covid-data/', covid_data, name='covid_data'),
    path('covid-data-post/', covid_data_post, name='covid_data_post'),
    path('', views.index, name='index'),
]
