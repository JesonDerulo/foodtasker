from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Restaurants(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE, related_name='restaurant')
    name        = models.CharField(max_length=500)
    phone       = models.CharField(max_length=500)
    address     = models.CharField(max_length=500)
    logo        = models.FileField(upload_to='restaurant_logo/', blank=True)

    def __str__(self):
        return self.name


