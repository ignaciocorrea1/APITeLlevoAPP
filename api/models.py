from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True, db_column="idUsuario")
    rut = models.CharField(max_length=12)
    nombres = models.CharField(max_length=80)
    paterno = models.CharField(max_length=30)
    materno = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    contrasenia = models.CharField(max_length=30)

    def __str__(self):
        return self.rut
    