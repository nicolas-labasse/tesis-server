from django.db import models


class PuntoInteres(models.Model):
    nombre = models.CharField(max_length=200)
    modelo = models.FileField(upload_to='modelos', null=True, blank=True)
    latitud = models.FloatField()
    longitud = models.FloatField()
    imagen = models.ImageField(upload_to='images', null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
