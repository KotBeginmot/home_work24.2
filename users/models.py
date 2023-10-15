from django.contrib.auth.models import AbstractUser
from django.db import models

from course.models import NULLABLE


# Create your models here.
class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    user_phone = models.CharField(max_length=20, verbose_name='phone number', **NULLABLE)
    user_city = models.CharField(max_length=20, verbose_name='city', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', **NULLABLE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}, {self.user_phone}'
