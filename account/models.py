from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.IntegerField(blank=True, null=True)
