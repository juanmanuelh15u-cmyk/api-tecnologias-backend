from django.contrib import admin
from .models import Tecnologia


@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'anio_creacion', 'activa']
    list_filter = ['categoria', 'activa']
    search_fields = ['nombre', 'descripcion']
    list_editable = ['activa']

# Register your models here.
