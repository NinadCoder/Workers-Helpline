from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from users.models import Profile
from .models import HireOffer

@login_required
def workers(request):
    all_workers = Profile.objects.filter(role='worker')
    return render(request, 'workers.html', {'workers': all_workers})

@login_required
def unskilled(request):
    unskilled_workers = Profile.objects.filter(role='worker', worker_type='general')
    return render(request, 'unskilled.html', {'workers': unskilled_workers})

@login_required
def skilled(request):
    skilled_workers = Profile.objects.filter(role='worker', worker_type='qualified')
    return render(request, 'skilled.html', {'workers': skilled_workers})

@login_required
def hire(request, user_id):
    # Only hirers can send offers
    if request.user.profile.role != 'hirer':
        return redirect('index')
    
    worker_detail = get_object_or_404(Profile, user__id=user_id, role='worker')
    
    if request.method == 'POST':
        offer_details = request.POST.get('offer_details', '').strip()
        # Fallback default if no custom details provided.
        if not offer_details:
            offer_details = "I would like to hire you for a job."
        HireOffer.objects.create(
            hirer=request.user,
            worker=worker_detail.user,
            offer_details=offer_details
        )
        return redirect('workers')
    
    return render(request, 'hire.html', {'worker_detail': worker_detail})


@login_required
def worker_offers(request):
    # Only workers can view offers they've received
    if request.user.profile.role != 'worker':
        return redirect('index')
    offers = HireOffer.objects.filter(worker=request.user).order_by('-date_offered')
    return render(request, 'worker_offers.html', {'offers': offers})

@login_required
def offer_action(request, offer_id):
    # Only allow workers to update their offers
    if request.user.profile.role != 'worker':
        return redirect('index')
    
    offer = get_object_or_404(HireOffer, id=offer_id, worker=request.user)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'accept':
            offer.status = 'accepted'
            offer.save()
            send_mail(
                'Your Offer Was Accepted',
                f'Hello {offer.hirer.username},\n\nYour offer to hire {offer.worker.username} has been accepted.',
                settings.DEFAULT_FROM_EMAIL,
                [offer.hirer.email],
                fail_silently=True,
            )
        elif action == 'reject':
            offer.status = 'rejected'
            offer.save()
            send_mail(
                'Your Offer Was Rejected',
                f'Hello {offer.hirer.username},\n\nYour offer to hire {offer.worker.username} has been rejected.',
                settings.DEFAULT_FROM_EMAIL,
                [offer.hirer.email],
                fail_silently=True,
            )
        return redirect('worker_offers')
    return redirect('worker_offers')

@login_required
def hirer_offers(request):
    # Only hirers can view offers they've sent
    if request.user.profile.role != 'hirer':
        return redirect('index')
    offers = HireOffer.objects.filter(hirer=request.user).order_by('-date_offered')
    return render(request, 'hirer_offers.html', {'offers': offers})
