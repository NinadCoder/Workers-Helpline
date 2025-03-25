from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()  # Save the user instance
            role = form.cleaned_data.get('role')
            # If you have an auto-created profile (via signals), update it.
            # Otherwise, create a new Profile for the user.
            try:
                profile = user.profile
            except Profile.DoesNotExist:
                profile = Profile(user=user)
            profile.role = role
            profile.save()
            messages.success(request, f'Account created for {user.username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def profile(request):
    if request.user.profile.role == 'worker':
        return render(request, 'worker_profile.html')
    else:
        return render(request, 'profile.html')
