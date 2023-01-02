from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Personal, Reservation


class PersonalFrom(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['email', 'password', 'name', 'phone',
                  'street', 'city', 'sex', 'bday', 'bmonth', 'byear']


# class ReservationForm(forms.ModelForm):
#     class Meta:
#         model = Reservation
#         fields = ['cld', 'seat']
