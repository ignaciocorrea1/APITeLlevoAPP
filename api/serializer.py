from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viaje
        fields = '__all__'

class DetalleViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleViaje
        fields = '__all__'
class SolicitudViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudViaje
        fields = '__all__'