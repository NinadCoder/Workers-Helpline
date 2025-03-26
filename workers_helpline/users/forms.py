from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(
        choices=Profile.ROLE_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )
    # Extra fields for workers
    worker_type = forms.ChoiceField(
        choices=Profile.WORKER_TYPE_CHOICES,
        widget=forms.RadioSelect,
        required=False
    )
    job_profession = forms.CharField(max_length=255, required=False)
    age = forms.IntegerField(required=False)
    address = forms.CharField(max_length=255, required=False)
    wage = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    police_verified = forms.BooleanField(required=False)
    
    # New field for the profile image
    profile_image = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = [
            'username', 'email', 'role', 'worker_type', 
            'job_profession', 'age', 'address', 'wage', 'police_verified',
            'profile_image', 'password1', 'password2'
        ]
