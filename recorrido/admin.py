from django.contrib import admin
from .models import Recorrido

# Register your models here.
@admin.register(Recorrido)
class RecorridoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'descripcion', 'duracion', 'activo')
    search_fields = ('nombre', 'descripcion')
