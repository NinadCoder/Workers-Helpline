from django.db import models
from django.conf import settings

STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected'),
)

class HireOffer(models.Model):
    hirer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='offers_sent'
    )
    worker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='offers_received'
    )
    offer_details = models.TextField(blank=True, null=True)
    date_offered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Offer from {self.hirer.username} to {self.worker.username} - {self.get_status_display()}"