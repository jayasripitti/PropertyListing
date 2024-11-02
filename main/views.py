# main/views.py
from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def properties(request):
    return render(request, 'main/properties.html')


def attractions(request):
    return render(request, 'main/attractions.html')
