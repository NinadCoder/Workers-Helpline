from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()  # Save the User instance
            role = form.cleaned_data.get('role')
            try:
                profile = user.profile
            except Profile.DoesNotExist:
                profile = Profile(user=user)
            profile.role = role
            if role == 'worker':
                profile.worker_type = form.cleaned_data.get('worker_type')
                profile.job_profession = form.cleaned_data.get('job_profession')
                profile.age = form.cleaned_data.get('age')
                profile.address = form.cleaned_data.get('address')
                profile.wage = form.cleaned_data.get('wage')
                profile.police_verified = form.cleaned_data.get('police_verified')
            # Update profile image if provided
            if 'profile_image' in request.FILES:
                profile.image = request.FILES['profile_image']
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