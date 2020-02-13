from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serilizers, viewsets

from Profile import views

urlpatterns = [
    re_path(r'profiles_list/$', views.ProfileList.as_view()),
    #Hola soy cesar
]