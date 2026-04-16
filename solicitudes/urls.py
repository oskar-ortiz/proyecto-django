from django.urls import path

from . import views

app_name = "solicitudes"

urlpatterns = [
    path("registrar/", views.registrar_solicitud, name="registrar"),
    path("confirmacion/", views.confirmacion_solicitud, name="confirmacion"),
]
