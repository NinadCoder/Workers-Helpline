from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    ROLE_CHOICES = [
        ('worker', 'Worker'),
        ('hirer', 'Hirer'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='hirer')

    def __str__(self):
        return f'{self.user.username} Profile'
