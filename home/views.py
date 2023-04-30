from django.shortcuts import render
from django.template.defaultfilters import register

from restaurant.models import Restaurant


@register.filter(name="index_class")
def index_class(value):
    return "active" if value == 0 else ""


def index(request):
    restaurants = Restaurant.objects.filter(status=Restaurant.Status.ACTIVE).all()
    return render(request, 'home.html', dict(restaurants=restaurants))


def restaurant_detail(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    return render(request, 'restaurant.html', dict(restaurant=restaurant))
