from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import WorkerDetailForm
from .models import WorkerDetail

# Create your views here.
def workers(request):
    return render(request, 'workers.html')
def unskilled(request):
    return render(request, 'unskilled.html')
def skilled(request):
    return render(request, 'skilled.html')
def hire(request):
    return render(request, 'hire.html')

@login_required
def worker_profile(request):
    # Ensure that only workers can access this view
    if request.user.profile.role != 'worker':
        return redirect('profile')  # or show an error message

    # Get or create a WorkerDetail instance for the user
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
