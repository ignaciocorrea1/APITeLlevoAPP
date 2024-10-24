from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import *
from .models import *

# Create your views here.
class UsuarioViewSet(viewsets.ModelViewSet):
    # Lista de elementos a los que estoy accediendo
    queryset = Usuario.objects.all()

    # Clase serializadora
    serializer_class = UsuarioSerializer

    # Se agrega un soporte para los filtros
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    # Campos que se pueden filtrar
    filterset_fields = ["correo", "contrasenia"]


