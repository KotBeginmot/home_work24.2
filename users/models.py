from django.contrib.auth.models import AbstractUser
from django.db import models

from course.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    user_phone = models.CharField(max_length=20, verbose_name='phone number', **NULLABLE)
    user_city = models.CharField(max_length=20, verbose_name='city', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', **NULLABLE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    course = models.ForeignKey('course.Course', on_delete=models.SET_NULL, verbose_name='курсы студента', **NULLABLE,
                               related_name='students')

    def __str__(self):
        return f'{self.email}, {self.user_phone}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('id',)
