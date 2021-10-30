from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager
from rental.models import Company


class CustomUser(AbstractUser):
    phone = models.IntegerField(null=True)
    ci = models.CharField(max_length=30, unique=True)

    # The company it's a member of
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True)

    USERNAME_FIELD = "username"

    objects = CustomUserManager()

    def __str__(self):
        return self.username
