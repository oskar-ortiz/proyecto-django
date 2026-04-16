from django.test import TestCase
from django.urls import reverse

from .models import Asistencia


class AsistenciaViewsTest(TestCase):
    def test_get_formulario(self):
        response = self.client.get(reverse("asistencia:registrar"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Registrar Asistencia")

    def test_post_guarda_asistencia(self):
        response = self.client.post(
            reverse("asistencia:registrar"),
            {
                "nombre_estudiante": "Ana Perez",
                "codigo_estudiante": "A001",
                "fecha": "2026-04-16",
                "estado": "presente",
                "observacion": "Llego puntual",
            },
        )

        self.assertRedirects(response, reverse("asistencia:confirmacion"))
        self.assertEqual(Asistencia.objects.count(), 1)
