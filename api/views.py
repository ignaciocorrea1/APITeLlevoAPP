from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as django_filters
from .serializer import *
from .models import *

# Create your views here.
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["idUsuario", "correo", "contrasenia"]

class ViajeFilter(django_filters.FilterSet):
    estado = django_filters.CharFilter(method='filter_estado')
    
    # Los fields filtran por conductor y viaje especificos
    class Meta:
        model = Viaje
        fields = {
            'conductor': ['exact'],
            'idViaje': ['exact'],
        }
    
    def filter_estado(self, queryset, name, value):
        # Si el valor del estado en la solicitud es activo se filtra por iniciado o en ruta
        if value == 'activo':
            return queryset.filter(estado__in=['iniciado', 'en ruta'])
        # Si el estado es distinto se filtra por ese estado
        return queryset.filter(estado=value)

class ViajeViewSet(viewsets.ModelViewSet):
    queryset = Viaje.objects.all()
    serializer_class = ViajeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ViajeFilter

    # Filtrar por viaje en iniciado o en ruta
    def get_queryset(self):
        queryset = Viaje.objects.all()
        conductor = self.request.query_params.get('conductor', None)
        estado = self.request.query_params.get('estado', None)

        if conductor is not None:
            queryset = queryset.filter(conductor=conductor)

        # Si el estado es 'activo', se filtra por ambos estados
        if estado == 'activo':  
            queryset = queryset.filter(estado__in=['iniciado', 'en ruta'])

        # Si es otro estado, se filtra por ese estado
        elif estado is not None:  
            queryset = queryset.filter(estado=estado)
            
        return queryset

    # Solicitudes POST
    def create(self, request, *args, **kwargs):
        # Obtencion de las iDs
        conductor_id = request.data.get("conductor_id")
        costoPersona = request.data.get("costoPersona")
        capacidadActual = request.data.get("capacidadActual")
        capacidadMaxima = request.data.get("capacidadMaxima")
        direccionInicio = request.data.get("direccionInicio")
        direccionFinal = request.data.get("direccionFinal")
        coordenadasInicioLat = request.data.get("coordenadasInicioLat")
        coordenadasInicioLng = request.data.get("coordenadasInicioLng")
        coordenadasFinalLat = request.data.get("coordenadasFinalLat")
        coordenadasFinalLng = request.data.get("coordenadasFinalLng")
        horaInicio = request.data.get("horaInicio")
        estado = request.data.get("estado")

        try:
            # Se buscan las instancias
            conductor = Usuario.objects.get(idUsuario = conductor_id)

            # Se crea la instancia nueva
            viaje = Viaje.objects.create(
                conductor = conductor,
                costoPersona = costoPersona,
                capacidadActual = capacidadActual,
                capacidadMaxima = capacidadMaxima,
                direccionInicio = direccionInicio,
                direccionFinal = direccionFinal,
                coordenadasInicioLat = coordenadasInicioLat,
                coordenadasInicioLng = coordenadasInicioLng,
                coordenadasFinalLat = coordenadasFinalLat,
                coordenadasFinalLng = coordenadasFinalLng,
                horaInicio = horaInicio,
                estado = estado
            )

            # Se serializa el detalle
            serializer = self.get_serializer(viaje)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        except Usuario.DoesNotExist:
            return Response(
                {"error": "El usuario especificado no existe"}, 
                status=status.HTTP_404_NOT_FOUND
            )
    
class DetalleViajeViewSet(viewsets.ModelViewSet):
    queryset = DetalleViaje.objects.all()
    serializer_class = DetalleViajeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["idViaje"]

    # Solicitudes POST
    def create(self, request, *args, **kwargs):
        # Obtencion de las iDs
        viaje_id = request.data.get("viaje_id")
        pasajero_id = request.data.get("pasajero_id")

        try:
            # Se buscan las instancias
            viaje = Viaje.objects.get(idViaje = viaje_id)
            pasajero = Usuario.objects.get(idUsuario = pasajero_id)

            # Se crea la instancia nueva
            detalle = DetalleViaje.objects.create(
                idViaje = viaje,
                pasajero = pasajero,
            )

            # Se serializa el detalle
            serializer = self.get_serializer(detalle)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        except Viaje.DoesNotExist:
            return Response(
                {"error": "El viaje especificado no existe"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Usuario.DoesNotExist:
            return Response(
                {"error": "El usuario especificado no existe"}, 
                status=status.HTTP_404_NOT_FOUND
            )
    
class SolicitudViajeViewSet(viewsets.ModelViewSet):
    queryset = SolicitudViaje.objects.all()
    serializer_class = SolicitudViajeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["viaje", "pasajero"]

    # Solicitudes POST
    def create(self, request, *args, **kwargs):
        # Obtencion de las IDs
        viaje_id = request.data.get("viaje_id")
        pasajero_id = request.data.get("pasajero_id")
        estado = request.data.get("estado")

        try:
            # Se buscan las instancias
            viaje = Viaje.objects.get(idViaje = viaje_id)
            pasajero = Usuario.objects.get(idUsuario = pasajero_id)

            # Se crea la instancia nueva
            solicitud = SolicitudViaje.objects.create(
                viaje = viaje,
                pasajero = pasajero,
                estado = estado
            )

            # Se serializa la solicitud
            serializer = self.get_serializer(solicitud)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        except Viaje.DoesNotExist:
            return Response(
                {"error": "El viaje especificado no existe"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Usuario.DoesNotExist:
            return Response(
                {"error": "El usuario especificado no existe"}, 
                status=status.HTTP_404_NOT_FOUND
            )
    
    # Solicitudes PUT
    def update(self, request, *args, **kwargs):
        # Obtencion de las IDs y la solicitud
        solicitud = self.get_object()
        viaje_id = request.data.get("viaje_id")
        pasajero_id = request.data.get("pasajero_id")
        estado = request.data.get("estado")

        try:
            # Se buscan las instancias
            viaje = Viaje.objects.get(idViaje = viaje_id)
            pasajero = Usuario.objects.get(idUsuario = pasajero_id)
            
            # Se asocian las instancias a la solicitud
            solicitud.viaje = viaje
            solicitud.pasajero = pasajero
            solicitud.estado = estado

            # Se guarda la instancia
            solicitud.save()

            # Se serializa la solicitud
            serializer = self.get_serializer(solicitud)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        except Viaje.DoesNotExist:
            return Response(
                {"error": "El viaje especificado no existe"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Usuario.DoesNotExist:
            return Response(
                {"error": "El usuario especificado no existe"}, 
                status=status.HTTP_404_NOT_FOUND
            )
