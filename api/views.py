from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import *
from .models import *

# Create your views here.
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["correo", "contrasenia"]

class ViajeViewSet(viewsets.ModelViewSet):
    queryset = Viaje.objects.all()
    serializer_class = ViajeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["conductor", "estado"]
    
class DetalleViajeViewSet(viewsets.ModelViewSet):
    queryset = DetalleViaje.objects.all()
    serializer_class = DetalleViajeSerializer
    
class SolicitudViajeViewSet(viewsets.ModelViewSet):
    queryset = SolicitudViaje.objects.all()
    serializer_class = SolicitudViajeSerializer
