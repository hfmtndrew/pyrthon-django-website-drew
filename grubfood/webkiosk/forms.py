from django.forms import ModelForm
from .models import Food
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'description', 'price']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']