from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='user_profile/', blank=True, null=True)
    phone_number = models.CharField(max_length=11)
    


class SiteAdmin(User):
    description = models.TextField(null=True, blank=True, default="")

    def __str__(self):
        return self.username
    
    class Meta:
            verbose_name = "Site Admin"
            verbose_name_plural = "Site Admins"


class Customer(User):
    is_vip = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"