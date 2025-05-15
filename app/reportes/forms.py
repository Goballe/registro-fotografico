from django import forms
from .models import ReporteFotografico

class ReporteForm(forms.ModelForm):
    class Meta:
        model = ReporteFotografico
        fields = [
            'proyecto', 'cliente', 'contratista', 'codigo_proyecto', 'version_reporte',
            'fecha_emision', 'elaborado_por', 'revisado_por', 'inicio_supervision',
            'mes_actual_obra', 'reporte_numero', 'descripcion',
            'foto1', 'foto2', 'foto3', 'foto4'
        ]
        widgets = {
            'fecha_emision': forms.DateInput(attrs={'type': 'date'}),
            'inicio_supervision': forms.DateInput(attrs={'type': 'date'})
        }
