"""
URL configuration for ibomma project.

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
from django.conf import settings
from django.conf.urls.static import static
from app.views import *
urlpatterns = [
    path("admin/", admin.site.urls),
    path('home/',Home.as_view(),name='Home'),
    path('tamil/',Tamil.as_view(),name='Tamil'),
    path('hindi/',Hindi.as_view(),name='Hindi'),
    path('about/',About.as_view(),name='About'),
    path('bug/',Bug.as_view(),name='Bug'),
    path('enter_Page/',Enter_Page.as_view(),name='Enter_Page'),
    path('',Login, name='Login'),
    path('registration/',registration,name='registration'),
    path('change_pas/',Change_pas,name='Change_pas'),
    path('reset_password/',reset_password,name='reset_password'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 