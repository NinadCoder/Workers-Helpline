from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    ROLE_CHOICES = [
        ('worker', 'Worker'),
        ('hirer', 'Hirer'),
    ]
    WORKER_TYPE_CHOICES = [
        ('qualified', 'Skilled Worker'),
        ('general', 'Unskilled Worker'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='hirer')
    
    # Extra worker details – only applicable if role == 'worker'
    worker_type = models.CharField(max_length=20, choices=WORKER_TYPE_CHOICES, blank=True, null=True)
    job_profession = models.CharField(max_length=255, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    wage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    police_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user.username} Profile'
