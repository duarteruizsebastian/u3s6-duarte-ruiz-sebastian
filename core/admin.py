from django.contrib import admin
from .models import Servicio

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'precio', 'propietario', 'creado_en')
    search_fields = ('titulo', 'categoria', 'propietario__username')
