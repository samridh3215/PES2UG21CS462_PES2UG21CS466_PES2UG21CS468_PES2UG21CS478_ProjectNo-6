from django.db import models
from django.utils import timezone

# Create your models here.
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.payment_id