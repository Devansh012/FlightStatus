from django.db import models
from .notifications import send_notification

class Flight(models.Model):
    number = models.CharField(max_length=10)
    status = models.CharField(max_length=20)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        send_notification(f'Flight {self.number} status updated to {self.status}')


    def __str__(self):
        return f'{self.number} - {self.status}'

