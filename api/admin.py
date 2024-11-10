from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Viaje)
admin.site.register(DetalleViaje)
admin.site.register(SolicitudViaje)