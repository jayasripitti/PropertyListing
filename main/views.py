# main/views.py
from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html', {'nbar': 'home'})


def about(request):
    return render(request, 'main/about.html', {'nbar': 'about'})


def properties(request):
    return render(request, 'main/properties.html', {'nbar': 'properties'})


def attractions(request):
    return render(request, 'main/attractions.html', {'nbar': 'attractions'})


def login(request):
    return render(request, 'main/login.html', {'nbar': 'login'})
