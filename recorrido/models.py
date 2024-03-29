from django.db import models
from pInteres.models import PuntoInteres

# Create your models here.

class Recorrido(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=1500)
    duracion = models.CharField(max_length=100, blank=True, null=True)
    puntoInteres = models.ManyToManyField(PuntoInteres)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre