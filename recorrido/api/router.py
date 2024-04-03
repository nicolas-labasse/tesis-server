from rest_framework.routers import DefaultRouter
from recorrido.api.views import RecorridoApiViewSet, RecorridoEstado
from django.urls import path, include

router = DefaultRouter()

router.register(r'', RecorridoApiViewSet, basename='recorrido')
router.register(r'estado_recorrido', RecorridoEstado, basename='estado-recorrido')


urlpatterns = [
    path('', include(router.urls)),
]