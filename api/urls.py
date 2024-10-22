from django.urls import path, include
from rest_framework import routers
from api import views

# Enrutador
router = routers.DefaultRouter()

# endpoint, viewsets para manejar las vistas correspondientes al endpoint
# se indica una r para evitar saltos de lineas con las /
router.register(r'usuarios', views.UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls))
]
