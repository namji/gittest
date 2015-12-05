from django.shortcuts import render
from django.http import Http404
from .models import Restaurant, Review

def index(request):
    return render(request, 'restaurants/index.html', {})

def indexb(request):
    return render(request, 'restaurants/index_b.html', {})

def list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/list.html', {"restaurants": restaurants})

def listb(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/list_b.html', {"restaurants": restaurants})

def detail(request, name):
    restaurant = Restaurant.objects.get(name=name)
    reviews = Review.objects.filter(restaurant=restaurant)
    return render(request, 'restaurants/detail.html', {"restaurant": restaurant, 'reviews': reviews})

def detailb(request, name):
    restaurant = Restaurant.objects.get(name=name)
    reviews = Review.objects.filter(restaurant=restaurant)
    return render(request, 'restaurants/detail_b.html', {"restaurant": restaurant, 'reviews': reviews})


def rating(request, value):
    rating_value = float(value)
    restaurants = Restaurant.objects.filter(rating__gte=rating_value)
    return render(request, 'restaurants/rating.html', {"restaurants": restaurants, "rating_value": rating_value})

def ratingb(request, value):
    rating_value = float(value)
    restaurants = Restaurant.objects.filter(rating__gte=rating_value)
    return render(request, 'restaurants/rating_b.html', {"restaurants": restaurants, "rating_value": rating_value})
