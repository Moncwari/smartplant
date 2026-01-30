from django.db import models
from django.conf import settings


class CareSchedule(models.Model):
    """Расписание ухода"""
    CARE_TYPES = [
        ('water', 'Полив'),
        ('fertilize', 'Подкормка'),
        ('mist', 'Опрыскивание'),
        ('repot', 'Пересадка'),
        ('prune', 'Обрезка'),
    ]
    
    plant = models.ForeignKey(
        'plants.Plant',
        on_delete=models.CASCADE,
        related_name='care_schedules'
    )
    
    care_type = models.CharField(max_length=20, choices=CARE_TYPES)
    frequency_days = models.PositiveIntegerField(
        help_text="Каждые N дней (например: 7)"
    )
    
    last_performed = models.DateTimeField(null=True, blank=True)
    next_due = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        unique_together = ['plant', 'care_type']
        verbose_name = "Расписание ухода"
        verbose_name_plural = "Расписания ухода"
    
    def __str__(self):
        return f"{self.get_care_type_display()} для {self.plant.nickname}"


class CareEvent(models.Model):
    """История ухода"""
    schedule = models.ForeignKey(
        CareSchedule,
        on_delete=models.CASCADE,
        related_name='events'
    )
    
    performed_at = models.DateTimeField(auto_now_add=True)
    performed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    
    notes = models.TextField(blank=True)
    skipped = models.BooleanField(default=False)
    
    def __str__(self):
        action = "пропущено" if self.skipped else "выполнено"
        return f"{self.schedule.get_care_type_display()} {action}"