from django.contrib import admin
from .models import Restaurants, Customer, Driver

# Register your models here.
admin.site.register(Restaurants)
admin.site.register(Driver)
admin.site.register(Customer)
