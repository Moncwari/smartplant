from django.db import models
from django.conf import settings


class Species(models.Model):
    """Справочник видов растений"""
    latin_name = models.CharField(max_length=200, unique=True)
    common_names = models.CharField(
        max_length=500, 
        help_text="Народные названия через запятую",
        blank=True
    )
    
    # Требования к уходу в формате JSON
    care_profile = models.JSONField(
        default=dict,
        help_text='Пример: {"light": "bright", "water": "moderate", "temp": "18-25"}'
    )
    
    difficulty = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)],
        default=3,
        help_text="Сложность ухода (1-легко, 5-сложно)"
    )
    
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Вид растения"
        verbose_name_plural = "Виды растений"
        ordering = ['latin_name']
    
    def __str__(self):
        return self.latin_name


class Plant(models.Model):
    """Конкретное растение пользователя"""
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='plants'
    )
    
    species = models.ForeignKey(
        Species,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='plants'
    )
    
    nickname = models.CharField(
        max_length=100,
        help_text="Как ты называешь это растение"
    )
    
    location_at_home = models.CharField(
        max_length=100,
        blank=True,
        help_text="Где стоит (например: Гостиная, южное окно)"
    )
    
    acquired_date = models.DateField(null=True, blank=True)
    pot_size_cm = models.PositiveIntegerField(null=True, blank=True)
    
    is_public = models.BooleanField(
        default=False,
        help_text="Показывать ли в публичном профиле"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        if self.species:
            return f"{self.nickname} ({self.species.latin_name})"
        return self.nickname