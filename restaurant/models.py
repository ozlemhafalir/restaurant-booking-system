from cloudinary.models import CloudinaryField
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models

from management.models import City, Cuisine


# Create your models here.


class Restaurant(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending'
        APPROVED = 'approved'
        ACTIVE = 'active'

    name = models.CharField(max_length=256)
    description = models.CharField(max_length=2048)
    address = models.CharField(max_length=1024)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='cities')
    cuisines = models.ManyToManyField(Cuisine, related_name='restaurants')
    status = models.CharField(max_length=64, choices=Status.choices, default=Status.PENDING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    menu = CloudinaryField('image', null=True)

    def __str__(self):
        return self.name


class RestaurantImage(models.Model):
    image = CloudinaryField('image')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='images')


class Table(models.Model):
    name = models.CharField(max_length=128)
    restaurant = models.ForeignKey(Restaurant, related_name='tables', on_delete=models.CASCADE)
    seats = models.IntegerField()

    def __str__(self):
        return self.name
