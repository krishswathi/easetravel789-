from django.db import models
from django.contrib.auth.models import User
import uuid

class BusCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    issued_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateField()

    def __str__(self):
        return f"{self.user.username}'s Card - {self.card_number}"

    def save(self, *args, **kwargs):
        if not self.card_number:
            self.card_number = str(uuid.uuid4().int)[:16]
        super().save(*args, **kwargs)
