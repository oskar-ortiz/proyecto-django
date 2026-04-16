from django.contrib import admin

from .models import Solicitud


@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_estudiante",
        "codigo_estudiante",
        "tipo_solicitud",
        "fecha_solicitud",
        "estado",
    )
    list_filter = ("estado", "fecha_solicitud")
    search_fields = ("nombre_estudiante", "codigo_estudiante", "tipo_solicitud")
