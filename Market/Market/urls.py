from . import views

from django.contrib import admin
from django.urls import path


# Patrones de URL
urlpatterns = [
    path('admin/', admin.site.urls),
# Función path, recibe dos parametros
# Definir la ruta de inicio
# Crear archivo view.py
    path('inicio/ ', views.inicio)
]
