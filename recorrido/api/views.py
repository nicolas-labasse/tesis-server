from rest_framework.viewsets import ModelViewSet
from pInteres.models import PuntoInteres
from recorrido.models import Recorrido
from recorrido.api.serializers import RecorridoSerializer, EstadoRecorridoSerializer
from rest_framework.response import Response
from rest_framework import status
from math import radians, sin, cos, sqrt, atan2


class RecorridoApiViewSet(ModelViewSet):
    queryset = Recorrido.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return RecorridoSerializer
        return RecorridoSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        puntos_ids = data.getlist('puntoInteres', [])
        data.pop('puntoInteres', None)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        recorrido = self.perform_create(serializer, puntos_ids)

        headers = self.get_success_headers(serializer.data)
        return Response(RecorridoSerializer(recorrido).data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = request.data.copy()

        puntos_ids = data.getlist('puntoInteres', [])
        data.pop('puntoInteres', None)

        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer, puntos_ids)

        return Response(serializer.data)
    
    def perform_update(self, serializer, puntos_ids):
        recorrido = serializer.save()

        recorrido.puntoInteres.clear()

        self._update_puntos(recorrido, puntos_ids)

    def _update_puntos(self, recorrido, puntos_ids):
        for punto_id in puntos_ids:
            try:
                punto = PuntoInteres.objects.get(id=punto_id)
                recorrido.puntoInteres.add(punto)
            except PuntoInteres.DoesNotExist:
                print(f'Punto de interés con ID {punto_id} no encontrado.')
    
    def perform_create(self, serializer, puntos_ids):
        recorrido = serializer.save()


        for punto_id in puntos_ids:
            try:
                punto = PuntoInteres.objects.get(id=punto_id)
                recorrido.puntoInteres.add(punto)
            except PuntoInteres.DoesNotExist:
                print(f'Punto de interés con ID {punto_id} no encontrado.')

        return recorrido


class RecorridoEstado(ModelViewSet):
    queryset = Recorrido.objects.all()
    serializer_class = EstadoRecorridoSerializer

    def update(self, request, *args, **kwargs):
        try:
            recorrido = self.get_object()
            data = request.data
            data['activo'] = False if recorrido.activo else True
            serializer = self.get_serializer(recorrido, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        except Exception as e:
            print('Exception:', e)
            return Response({'error': 'Error interno del servidor'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

"""class RecorridoUbicacion(ModelViewSet):
    queryset = Recorrido.objects.all()
    serializer_class = RecorridoSerializer

    def get_queryset(self):
        latitud_str = self.request.query_params.get('latitud')
        longitud_str = self.request.query_params.get('longitud')

        if latitud_str is not None and longitud_str is not None:
            latitud = float(latitud_str)
            longitud = float(longitud_str)

            recorridos_cercanos = Recorrido.objects.filter(
                puntoInteres__latitud__range=(latitud - 0.1, latitud + 0.1),
                puntoInteres__longitud__range=(longitud - 0.1, longitud + 0.1)
            )[:5]
            
            return recorridos_cercanos

        return Recorrido.objects.none()"""

class RecorridoUbicacion(ModelViewSet):
    queryset = Recorrido.objects.all()
    serializer_class = RecorridoSerializer

    def get_queryset(self):
        latitud_str = self.request.query_params.get('latitud')
        longitud_str = self.request.query_params.get('longitud')

        if latitud_str is not None and longitud_str is not None:
            latitud = float(latitud_str)
            longitud = float(longitud_str)

            recorridos = Recorrido.objects.all()
            recorridos_cercanos = []

            for recorrido in recorridos:
                punto_cercano_encontrado = False
                for punto_interes in recorrido.puntoInteres.all():
                    distancia = haversine(latitud, longitud, punto_interes.latitud, punto_interes.longitud)
                    if distancia <= 6:
                        punto_cercano_encontrado = True
                        break  
                if punto_cercano_encontrado:
                    recorridos_cercanos.append(recorrido)
                    

            return recorridos_cercanos[:5]

        return Recorrido.objects.none()

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0

    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distancia = R * c
    return distancia





