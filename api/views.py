from rest_framework import viewsets
from .serializer import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
class UsuarioViewSet(viewsets.ModelViewSet):
    # Lista de elementos a los que estoy accediendo
    queryset = Usuario.objects.all()

    # Clase serializadora
    serializer_class = UsuarioSerializer


    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        print(response.data)  

        return response