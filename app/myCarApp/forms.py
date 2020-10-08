from django import forms
from django.contrib.auth.models import User
from myCarApp.models import LesseeProfile, LessorProfile, Car
from django.db import models
from django.forms import ModelForm, FileField

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password',)

class LesseeForm(forms.ModelForm):
    class Meta():
        model = LesseeProfile
        fields = ('driving_license','average_cc','cars_count')
        widgets = {'average_cc': forms.HiddenInput(),'cars_count': forms.HiddenInput}

class LessorForm(forms.ModelForm):
    class Meta():
        model = LessorProfile
        fields = ('id',)

class CarRegistrationForm(forms.ModelForm):
    class Meta():
        model = Car
        photo = forms.ImageField
        fields = ('brand', 'model', 'CC', 'year','color', 'transmission', 'fuelType', 'firstAvailableDay', 'lastAvailableDay', 'pricePerDay', 'photo')
        widgets = {
            'firstAvailableDay': forms.SelectDateWidget(),
            'lastAvailableDay': forms.SelectDateWidget(),
        }


