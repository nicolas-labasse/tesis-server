from rest_framework.serializers import ModelSerializer
from calificacion.api import serializers
from pInteres.models import PuntoInteres

class PuntoInteresSerializer(ModelSerializer):
    class Meta:
        model = PuntoInteres
        fields = ('id', 'nombre', 'modelo', 'latitud', 'longitud', 'imagen', 'activo')

class EstadoPuntoInteresSerializer(ModelSerializer):
    class Meta:
        model = PuntoInteres
        fields = ['activo']
