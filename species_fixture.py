import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.plants.models import Species

# Список популярных растений
species_data = [
    {
        "latin_name": "Monstera deliciosa",
        "common_names": "Монстера, Швейцарский сырный завод",
        "care_profile": {
            "light": "bright_indirect",
            "water": "moderate",
            "humidity": "high",
            "temp": "18-27"
        },
        "difficulty": 2,
        "description": "Популярное комнатное растение с характерными дырявыми листьями."
    },
    {
        "latin_name": "Ficus lyrata",
        "common_names": "Фикус лировидный, Фикус скрипка",
        "care_profile": {
            "light": "bright",
            "water": "moderate",
            "humidity": "medium",
            "temp": "16-24"
        },
        "difficulty": 3,
        "description": "Крупное растение с листьями в форме скрипки. Любит свет."
    },
    {
        "latin_name": "Sansevieria trifasciata",
        "common_names": "Сансевиерия, Тещин язык, Змеиное растение",
        "care_profile": {
            "light": "low_to_bright",
            "water": "low",
            "humidity": "low",
            "temp": "15-30"
        },
        "difficulty": 1,
        "description": "Неубиваемое растение, переносит тень и редкий полив."
    },
    {
        "latin_name": "Spathiphyllum",
        "common_names": "Спатифиллум, Женское счастье",
        "care_profile": {
            "light": "low_to_medium",
            "water": "high",
            "humidity": "high",
            "temp": "18-24"
        },
        "difficulty": 2,
        "description": "Цветет белыми цветами. Любит влажность и не любит пересыхания."
    },
    {
        "latin_name": "Zamioculcas zamiifolia",
        "common_names": "Замиокулькас, Долларовое дерево",
        "care_profile": {
            "light": "low_to_bright",
            "water": "low",
            "humidity": "low",
            "temp": "16-26"
        },
        "difficulty": 1,
        "description": "Суккулент с глянцевыми листьями. Может пережить месяц без полива."
    }
]

# Загружаем в базу
for data in species_data:
    Species.objects.get_or_create(
        latin_name=data["latin_name"],
        defaults=data
    )

print("✅ Загружено видов растений:", Species.objects.count())