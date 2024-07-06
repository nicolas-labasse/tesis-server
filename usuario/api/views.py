from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from usuario.models import Usuario
from usuario.api.serializers import UsuarioSerializer, UsuarioFavoritoSerializer, EditarImagenUsuarioSerializer, EditarUsuarioNombreSerializer, EstadoUsuarioSerializer
import requests
from django.core.files.base import ContentFile
import mimetypes

"""class UsuarioApiViewSet(ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            print('Exception:', e)
            return Response({'error': 'Error interno del servidor no entre al try'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)"""



class UsuarioApiViewSet(ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            data = request.data.copy()  # Make a mutable copy of the request data
            image_url = data.get('imagen')  # Assuming 'imagen' is the field name for the image URL

            if image_url and isinstance(image_url, str):  # Check if the image field is a URL (string)
                print(f'Debug: image_url is a string: {image_url}')
                try:
                    response = requests.get(image_url)
                    response.raise_for_status()  # Raise an error for bad status codes
                    content_type = response.headers['Content-Type']
                    extension = mimetypes.guess_extension(content_type)
                    if not extension:
                        extension = ".png"  # Default extension if none can be guessed
                    file_name = image_url.split('/')[-1].split('?')[0]
                    if not file_name.endswith(extension):
                        file_name += extension
                    data['imagen'] = ContentFile(response.content, file_name)
                    print(f'Debug: Image downloaded and content file created: {file_name}')
                except requests.RequestException as e:
                    print(f'Debug: Error downloading the image: {e}')
                    return Response({'error': f'Error al descargar la imagen: {e}'}, status=status.HTTP_400_BAD_REQUEST)

            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            print(f'Debug: Exception in create method: {e}')
            return Response({'error': 'Error interno del servidor'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class UsuarioFavoritoAPIView(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioFavoritoSerializer
    def put(self, request, id_usuario):
        try:
            usuario = self.get_object()
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditarImagenUsuario(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = EditarImagenUsuarioSerializer

    def update(self, request, *args, **kwargs):
        try:
            usuario = self.get_object()
            data = request.data
                
            imagen_url = data.get('imagen_update', '')

            data['imagen_url'] = imagen_url

            serializer = self.get_serializer(usuario, data=data, partial=True)
            serializer.is_valid(raise_exception=True)

            usuario.imagen = data.get('imagen_url', usuario.imagen)
            self.perform_update(serializer)

            return Response(serializer.data)
        except Exception as e:
            print('Exception:', e)
            return Response({'error': 'Error interno del servidor'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class EditarUsuarioNombre(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = EditarUsuarioNombreSerializer

    def update(self, request, *args, **kwargs):
        try:
            usuario = self.get_object()
            
            data = request.data.dict() 
            data['nombre'] = request.data.get('nombre', usuario.nombre)  

            serializer = self.get_serializer(usuario, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        except Exception as e:
            print('Exception:', e)
            return Response({'error': 'Error interno del servidor'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class EstadoUsuario(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = EstadoUsuarioSerializer

    def update(self, request, *args, **kwargs):
        try:
            usuario = self.get_object()
            data = request.data
            data['activo'] = False if usuario.activo else True
            serializer = self.get_serializer(usuario, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        except Exception as e:
            print('Exception:', e)
            return Response({'error': 'Error interno del servidor'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


