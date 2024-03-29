from django.db import models

# Create your models here.

class CustomerAccount(models.Model):
    email = models.EmailField(unique=True, blank=False, verbose_name="Email")
    passwd  = models.CharField(blank=False, verbose_name="Password", max_length=100)




