from django.contrib import admin
from .models import Species, Plant

@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('latin_name', 'difficulty')
    search_fields = ('latin_name', 'common_names')

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'species', 'owner', 'created_at')
    list_filter = ('owner', 'species')
    search_fields = ('nickname',)