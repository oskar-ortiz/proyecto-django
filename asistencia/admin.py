from django.contrib import admin

from .models import Asistencia


@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ("nombre_estudiante", "codigo_estudiante", "fecha", "estado")
    list_filter = ("estado", "fecha")
    search_fields = ("nombre_estudiante", "codigo_estudiante")
