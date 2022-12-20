from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # first_name = models.CharField(max_length=200, null=True)
    # last_name = models.CharField(max_length=200, null=True)
    # phone = models.CharField(max_length=12, null=True)
    # email = models.EmailField(max_length=100, unique=True)
    pass