from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    school_principal = models.CharField(max_length=50, default=' ', null=True, blank=True)
    cell_phone = models.CharField (max_length=50, default=' ', null=True, blank=True)

# Create your models here.
