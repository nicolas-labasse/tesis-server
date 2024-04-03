from rest_framework.serializers import ModelSerializer
from usuario.models import Usuario
from rest_framework import serializers

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','email', 'nombre', 'recorridoFavorito', 'imagen', 'ultimosRecorridos', 'activo']
        

class UsuarioFavoritoSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['recorridoFavorito']

class EditarImagenUsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['imagen']

class EditarUsuarioNombreSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre']

class EstadoUsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['activo']