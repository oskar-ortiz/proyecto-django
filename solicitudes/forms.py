from django import forms

from .models import Solicitud


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            "nombre_estudiante",
            "codigo_estudiante",
            "tipo_solicitud",
            "descripcion",
            "fecha_solicitud",
            "estado",
        ]
        widgets = {
            "descripcion": forms.Textarea(attrs={"rows": 4}),
            "fecha_solicitud": forms.DateInput(attrs={"type": "date"}),
        }
