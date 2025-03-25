from django.db import models
from django.contrib.auth.models import User

class WorkerDetail(models.Model):
    WORKER_TYPE_CHOICES = [
        ('qualified', 'Qualified Worker'),
        ('general', 'General Worker'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    worker_type = models.CharField(max_length=20, choices=WORKER_TYPE_CHOICES, default='general')
    address = models.CharField(max_length=255, blank=True, null=True)
    job_profession = models.CharField(max_length=255, blank=True, null=True)
    wage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    police_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.worker_type}"
