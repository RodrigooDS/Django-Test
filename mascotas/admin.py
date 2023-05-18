from django.contrib import admin

from .models import Animal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ("nombre", "raza", "sexo", "paciente")
    list_filter = ("raza", "sexo", "paciente")
    search_fields = ("nombre", "raza", "paciente__nombre")
