"""customer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from task import views as e
from destination import views
import requests

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api',e.Register),
    path('api1/<str:pk>',e.Update),
    path('api2/<str:pk>',e.Delete),
    path('api3/<str:pk>',e.get),
    path('api4',views.web),
    path('api5/<str:pk>',views.put),
    path('api6/<str:pk>',views.delete),
    path('api7/<str:pk>',views.get)
]
