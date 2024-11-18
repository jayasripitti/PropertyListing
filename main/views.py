from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html', {'nbar': 'home'})


def about(request):
    return render(request, 'main/about.html', {'nbar': 'about'})


def properties(request):
    return render(request, 'main/properties.html', {'nbar': 'properties'})


def attractions(request):
    return render(request, 'main/attractions.html', {'nbar': 'attractions'})


def admin(request):
    return render(request, 'main/admin_dashboard.html', {'nbar': 'admin_dashboard'})
