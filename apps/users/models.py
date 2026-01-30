from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    
    # Настройки уведомлений
    email_notifications = models.BooleanField(default=True)
    push_notifications = models.BooleanField(default=True)
    
    # Город (для будущей функции обмена растениями)
    city = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.username