from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ViajeSerializer(serializers.ModelSerializer):
    conductor = UsuarioSerializer(read_only=True)
    class Meta:
        model = Viaje
        fields = '__all__'

class DetalleViajeSerializer(serializers.ModelSerializer):
    pasajero = UsuarioSerializer(read_only=True)
    viaje = ViajeSerializer(read_only=True)
    
    class Meta:
        model = DetalleViaje
        fields = '__all__'
class SolicitudViajeSerializer(serializers.ModelSerializer):
    viaje = ViajeSerializer(read_only=True)
    pasajero = UsuarioSerializer(read_only=True)
    # Source indica que se debe mapear a ese dato el campo
    viaje_id = serializers.IntegerField(write_only=True, source='viaje')
    pasajero_id = serializers.IntegerField(write_only=True, source='pasajero')
    class Meta:
        model = SolicitudViaje
        fields = ['idSolicitud', 'viaje', 'pasajero', 'estado', 'viaje_id', 'pasajero_id']