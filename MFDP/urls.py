from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
    path('service', service, name="service"),
    path('team', team, name="team"),
    path('team_exe', team_exe, name="team_exe"),
    path('mission', mission, name="mission"),

]