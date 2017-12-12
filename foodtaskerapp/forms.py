from django import forms
from django.contrib.auth.models import User
from foodtaskerapp.models import Restaurants

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name','last_name', 'email')

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurants
        fields = ('name', 'phone', 'address', 'logo')