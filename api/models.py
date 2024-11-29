from django.db import models

# Create your models here.

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True, db_column="idUsuario")
    rut = models.CharField(max_length=12)
    nombres = models.CharField(max_length=80)
    paterno = models.CharField(max_length=30)
    materno = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    contrasenia = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.nombres} {self.paterno} {self.materno}"

class Viaje(models.Model):
    idViaje = models.AutoField(primary_key=True, db_column="idViaje")
    conductor = models.ForeignKey("Usuario", on_delete=models.CASCADE, db_column="idUsuario")
    costoPersona = models.IntegerField()
    capacidadActual = models.IntegerField(default=0)
    capacidadMaxima = models.IntegerField()
    direccionInicio = models.CharField(max_length=200)
    direccionFinal = models.CharField(max_length=200)
    coordenadasInicioLat = models.DecimalField(max_digits=15, decimal_places=10)
    coordenadasInicioLng = models.DecimalField(max_digits=15, decimal_places=10)
    coordenadasFinalLat = models.DecimalField(max_digits=15, decimal_places=10)
    coordenadasFinalLng = models.DecimalField(max_digits=15, decimal_places=10)
    horaInicio = models.TimeField()
    estado = models.CharField(max_length=30)

    def __str__(self):
        return f"Viaje de: {self.conductor.nombres} {self.conductor.paterno}"

class DetalleViaje(models.Model):
    idDetalle = models.AutoField(primary_key=True, db_column="idDetalle")
    idViaje = models.ForeignKey("Viaje", on_delete=models.CASCADE, db_column="idViaje")
    pasajero = models.ForeignKey("Usuario", on_delete=models.CASCADE, db_column="idUsuario")

    def __str__(self):
        return f"Detalle viaje de: {self.idViaje.conductor.nombres} {self.idViaje.conductor.paterno}"
    
class SolicitudViaje(models.Model):
    idSolicitud = models.AutoField(primary_key=True, db_column="idSolicitud")
    viaje = models.ForeignKey("Viaje", on_delete=models.CASCADE, db_column="idViaje")
    pasajero = models.ForeignKey("Usuario", on_delete=models.CASCADE, db_column="idUsuario")
    estado = models.CharField(max_length=30)

    def __str__(self):
        return f"Solicitud de: {self.pasajero.nombres} {self.pasajero.paterno} a viaje con id: {self.viaje}"
    