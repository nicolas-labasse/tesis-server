from django.contrib import admin
from .models import Usuario

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'nombre','imagen', 'recorridoFavorito', 'activo')
    search_fields = ('email', 'nombre')
