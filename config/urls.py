from django.contrib import admin
from django.urls import path
from apps.plants.views import my_plants, add_plant, water_plant

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_plants, name='home'),
    path('add/', add_plant, name='add_plant'),
    path('water/<int:plant_id>/', water_plant, name='water_plant'),  # Новый путь
]