from django.urls import path, include
from rest_framework import routers
from api import views

# Enrutador
router = routers.DefaultRouter()

# endpoint, viewsets para manejar las vistas correspondientes al endpoint
# se indica una r para evitar saltos de lineas con las /
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'viajes', views.ViajeViewSet)
router.register(r'detalles', views.DetalleViajeViewSet)
router.register(r'solicitudes', views.SolicitudViajeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
