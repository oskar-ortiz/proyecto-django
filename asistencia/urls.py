from django.urls import path

from . import views

app_name = "asistencia"

urlpatterns = [
    path("registrar/", views.registrar_asistencia, name="registrar"),
    path("confirmacion/", views.confirmacion_asistencia, name="confirmacion"),
]
