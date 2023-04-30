from django.urls import path

from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('restaurant/<int:pk>/', views.restaurant_detail, name='restaurant')
]
