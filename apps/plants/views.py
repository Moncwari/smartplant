from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from .models import Plant, Species
from apps.care.models import CareSchedule, CareEvent


@login_required
def my_plants(request):
    """Главная страница со списком растений"""
    plants = Plant.objects.filter(owner=request.user).select_related('species')
    
    # Для каждого растения проверим, нужен ли полив
    plants_with_status = []
    for plant in plants:
        # Ищем расписание полива
        schedule = CareSchedule.objects.filter(plant=plant, care_type='water').first()
        
        status = "ok"
        if schedule and schedule.next_due:
            if schedule.next_due < timezone.now():
                status = "overdue"  # Просрочено
        
        plants_with_status.append({
            'plant': plant,
            'schedule': schedule,
            'status': status
        })
    
    return render(request, 'plants/plant_list.html', {
        'plants_with_status': plants_with_status
    })


@login_required
def water_plant(request, plant_id):
    """Отметить полив растения"""
    plant = get_object_or_404(Plant, id=plant_id, owner=request.user)
    
    # Находим или создаем расписание полива
    schedule, created = CareSchedule.objects.get_or_create(
        plant=plant,
        care_type='water',
        defaults={'frequency_days': 7}  # По умолчанию раз в неделю
    )
    
    # Создаем событие "полив"
    CareEvent.objects.create(
        schedule=schedule,
        performed_by=request.user,
        notes="Полито через кнопку"
    )
    
    # Обновляем даты
    schedule.last_performed = timezone.now()
    schedule.next_due = timezone.now() + timedelta(days=schedule.frequency_days)
    schedule.save()
    
    return redirect('home')


@login_required
def add_plant(request):
    """Добавление нового растения"""
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        species_id = request.POST.get('species')
        location = request.POST.get('location')
        
        plant = Plant.objects.create(
            owner=request.user,
            nickname=nickname,
            species_id=species_id if species_id else None,
            location_at_home=location
        )
        
        # Сразу создаем расписание полива (раз в 7 дней по умолчанию)
        CareSchedule.objects.create(
            plant=plant,
            care_type='water',
            frequency_days=7,
            next_due=timezone.now() + timedelta(days=7)
        )
        
        return redirect('home')
    
    species_list = Species.objects.all()
    return render(request, 'plants/add_plant.html', {'species_list': species_list})