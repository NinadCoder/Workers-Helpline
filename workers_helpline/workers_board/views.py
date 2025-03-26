from django.shortcuts import render, get_object_or_404
from users.models import Profile

def workers(request):
    all_workers = Profile.objects.filter(role='worker')
    return render(request, 'workers.html', {'workers': all_workers})

def unskilled(request):
    unskilled_workers = Profile.objects.filter(role='worker', worker_type='general')
    return render(request, 'unskilled.html', {'workers': unskilled_workers})

def skilled(request):
    skilled_workers = Profile.objects.filter(role='worker', worker_type='qualified')
    return render(request, 'skilled.html', {'workers': skilled_workers})

from django.shortcuts import render, get_object_or_404
from users.models import Profile

def hire(request, user_id):
    # Get the worker's Profile based on the given user_id.
    worker_detail = get_object_or_404(Profile, user__id=user_id, role='worker')
    context = {
        'worker_detail': worker_detail,
    }
    return render(request, 'hire.html', context)
