from django.db import models


class Asistencia(models.Model):
    ESTADO_PRESENTE = "presente"
    ESTADO_AUSENTE = "ausente"
    ESTADO_TARDE = "tarde"
    ESTADO_CHOICES = [
        (ESTADO_PRESENTE, "Presente"),
        (ESTADO_AUSENTE, "Ausente"),
        (ESTADO_TARDE, "Tarde"),
    ]

    nombre_estudiante = models.CharField(max_length=100)
    codigo_estudiante = models.CharField(max_length=20)
    fecha = models.DateField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)
    observacion = models.TextField(blank=True)

    class Meta:
        ordering = ["-fecha", "nombre_estudiante"]

    def __str__(self):
        return f"{self.nombre_estudiante} - {self.fecha} - {self.estado}"
