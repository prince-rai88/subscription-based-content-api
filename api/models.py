from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    
    subsciption_choices=[("premium", "Premium"), ("free","Free")]
    subscription_type=models.CharField(max_length=20, choices=subsciption_choices, default="free")

    subscription_expiry_date=models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username
    



class PremiumAccessLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    endpoint = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.endpoint} - {self.timestamp}"

