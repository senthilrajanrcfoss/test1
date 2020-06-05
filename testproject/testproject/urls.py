"""testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from django.conf import settings
from rest_framework.routers import DefaultRouter
from todoapi.views import *

router = routers.DefaultRouter()
# router.register(r'customer',tbl_Customer,'customer')

urlpatterns = [
    # url(r'^rest/', include('lcm.urls')),
    url(r'^', include('todoapi.urls')),
    # url(r'^admin/', admin.site.urls),
    # url(r'^sadmin/auth/', include('cx_auth.urls')),  
]
