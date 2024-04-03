from rest_framework.viewsets import ModelViewSet
from pInteres.models import PuntoInteres
from recorrido.models import Recorrido
from recorrido.api.serializers import RecorridoSerializer, EstadoRecorridoSerializer
from rest_framework.response import Response
from rest_framework import status


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

