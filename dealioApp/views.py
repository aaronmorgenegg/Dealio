from django.shortcuts import render
from dealioApp.models import Restaurant

# Create your views here.


def index(request):
    return render(request, 'dealioApp/home.html') #render looks in templates directory


def restaurants(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'dealioApp/restaurants.html', {'restaurants': restaurants}) #render looks in templates directory #can pass in content into render() such as dictionaries


def promotions(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'dealioApp/promotions.html', {'restaurants': restaurants})