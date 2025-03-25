from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(
        choices=Profile.ROLE_CHOICES,
        widget=forms.RadioSelect,  # This displays as radio buttons
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password1', 'password2']
