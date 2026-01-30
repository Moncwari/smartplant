from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Переопределяем связи, чтобы избежать конфликта с auth.User
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_user_set',  # Уникальное имя
        related_query_name='custom_user',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set',  # Уникальное имя
        related_query_name='custom_user',
    )
    
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    email_notifications = models.BooleanField(default=True)
    push_notifications = models.BooleanField(default=True)
    city = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.username

# postgresql://smartplant_ha0w_user:2ZugEFexrYyk2rOYl2EbHwgwht1Q2Lmb@dpg-d5ucsf14tr6s73elt3pg-a/smartplant_ha0w