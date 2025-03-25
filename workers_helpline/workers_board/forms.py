from django import forms
from .models import WorkerDetail

class WorkerDetailForm(forms.ModelForm):
    class Meta:
        model = WorkerDetail
        fields = ['worker_type', 'address', 'job_profession', 'wage', 'police_verified']
