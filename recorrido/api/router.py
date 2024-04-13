from rest_framework.routers import DefaultRouter
from recorrido.api.views import RecorridoApiViewSet, RecorridoEstado, RecorridoUbicacion
from django.urls import path, include

router = DefaultRouter()

router.register(r'recorrido', RecorridoApiViewSet, basename='recorrido')
router.register(r'estado_recorrido', RecorridoEstado, basename='estado-recorrido')
router.register(r'ubicacion_recorrido', RecorridoUbicacion, basename='ubicacion-recorrido')