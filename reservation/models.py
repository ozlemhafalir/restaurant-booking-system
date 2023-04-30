from django.conf import settings
from django.db import models

from restaurant.models import Restaurant, Table


# Create your models here.

class Reservation(models.Model):
    class Status(models.TextChoices):
        NEW = 'new'
        ASSIGNED = 'assigned'
        CANCELLED = 'cancelled'
        DECLINED = 'declined'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    guests = models.IntegerField()
    notes = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reservations')
    status = models.CharField(max_length=64, choices=Status.choices, default=Status.NEW)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)