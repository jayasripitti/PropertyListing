# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('properties/', views.properties, name='properties'),
    path('attractions/', views.attractions, name='attractions'),
    path('login/', views.login, name='login'),
]
