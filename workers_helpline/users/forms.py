from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField

class UserRegisterForm(UserCreationForm):
    phone_number = PhoneNumberField(
        label='Phone Number',
        region='IN'  # sets India as the default region
    )
    class Meta:
        model = User
        fields = ['username', 'phone_number', 'password1', 'password2']