from rest_framework import viewsets
from .serializer import *
from .models import *

# Create your views here.
class UsuarioViewSet(viewsets.ModelViewSet):
    # Lista de elementos a los que estoy accediendo
    queryset = Usuario.objects.all()

    # Clase serializadora
    serializer_class = UsuarioSerializer