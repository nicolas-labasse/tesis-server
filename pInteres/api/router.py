from rest_framework.routers import DefaultRouter
from pInteres.api.views import PuntoInteresApiViewSet, EstadoPuntoInteres
from django.urls import include, path


router = DefaultRouter()

router.register(r'', PuntoInteresApiViewSet, basename='pInteres')
router.register(r'estado_puntoInteres', EstadoPuntoInteres, basename='estado-punto-interes')


urlpatterns = [
    path('', include(router.urls)),
]