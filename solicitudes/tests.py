from django.test import TestCase
from django.urls import reverse

from .models import Solicitud


class SolicitudViewsTest(TestCase):
    def test_get_formulario(self):
        response = self.client.get(reverse("solicitudes:registrar"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Registrar Solicitud")

    def test_post_guarda_solicitud(self):
        response = self.client.post(
            reverse("solicitudes:registrar"),
            {
                "nombre_estudiante": "Luis Gomez",
                "codigo_estudiante": "S001",
                "tipo_solicitud": "Certificado",
                "descripcion": "Solicitud de certificado academico",
                "fecha_solicitud": "2026-04-16",
                "estado": "pendiente",
            },
        )

        self.assertRedirects(response, reverse("solicitudes:confirmacion"))
        self.assertEqual(Solicitud.objects.count(), 1)
