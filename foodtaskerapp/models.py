from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Restaurants(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE, related_name='restaurant')
    name        = models.CharField(max_length=500)
    phone       = models.CharField(max_length=500)
    address     = models.CharField(max_length=500)
    logo        = models.FileField(upload_to='restaurant_logo/', blank=True)
    date        = models.DateTimeField(blank=True, null=True, default=timezone.now)


    def __str__(self):
        return self.name

class Customer(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    avatar      = models.CharField(max_length=500)
    phone       = models.CharField(max_length=500, blank=True)
    address     = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.user.get_full_name()

class Driver(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE, related_name='driver')
    avatar      = models.CharField(max_length=500)
    phone       = models.CharField(max_length=500, blank=True)
    address     = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.user.get_full_name()


