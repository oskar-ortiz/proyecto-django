from django.db import models


class Solicitud(models.Model):
    ESTADO_PENDIENTE = "pendiente"
    ESTADO_APROBADA = "aprobada"
    ESTADO_RECHAZADA = "rechazada"
    ESTADO_CHOICES = [
        (ESTADO_PENDIENTE, "Pendiente"),
        (ESTADO_APROBADA, "Aprobada"),
        (ESTADO_RECHAZADA, "Rechazada"),
    ]

    nombre_estudiante = models.CharField(max_length=100)
    codigo_estudiante = models.CharField(max_length=20)
    tipo_solicitud = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_solicitud = models.DateField()
    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default=ESTADO_PENDIENTE,
    )

    class Meta:
        ordering = ["-fecha_solicitud", "nombre_estudiante"]

    def __str__(self):
        return f"{self.nombre_estudiante} - {self.tipo_solicitud}"
