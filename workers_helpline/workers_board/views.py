from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import WorkerDetailForm
from .models import WorkerDetail

def workers(request):
    return render(request, 'workers.html')

def unskilled(request):
    # Filter for unskilled (general) workers
    unskilled_workers = WorkerDetail.objects.filter(worker_type='general')
    context = {'workers': unskilled_workers}
    return render(request, 'unskilled.html', context)

def skilled(request):
    # Filter for skilled (qualified) workers
    skilled_workers = WorkerDetail.objects.filter(worker_type='qualified')
    context = {'workers': skilled_workers}
    return render(request, 'skilled.html', context)

def hire(request):
    return render(request, 'hire.html')

def worker_detail_view(request, user_id):
    # Displays a single worker’s details
    worker_detail = get_object_or_404(WorkerDetail, user__id=user_id)
    context = {
        'worker_detail': worker_detail
    }
    return render(request, 'hire.html', context)

@login_required
def worker_profile(request):
    # Ensure that only users with role = "worker" can access
    if request.user.profile.role != 'worker':
        return redirect('profile')  # or show an error

    # Get or create a WorkerDetail instance for this user
    worker_detail, created = WorkerDetail.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = WorkerDetailForm(request.POST, instance=worker_detail)
        if form.is_valid():
            form.save()
            return redirect('worker_profile')
    else:
        form = WorkerDetailForm(instance=worker_detail)
    
    context = {
        'form': form,
        'worker_detail': worker_detail,
    }
    return render(request, 'worker_profile.html', context)
