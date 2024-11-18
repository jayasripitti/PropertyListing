from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('properties/', views.properties, name='properties'),
    path('attractions/', views.attractions, name='attractions'),
    path('admin_login/', LoginView.as_view(template_name='main/login.html'),name='admin_login'),
    path('accounts/profile/', views.admin, name='admin_dashboard'),
    path('accounts/profile/logout', views.home, name='logout'),
    # path('logout', views.home, name='logout'),
    # path('logout', LogoutView.as_view(template_name=views.home), name='logout'),
]
