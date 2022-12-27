from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Personal


class PersonalFrom(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['email', 'password', 'name', 'phone',
                  'street', 'city', 'sex', 'bday', 'bmonth', 'byear']
