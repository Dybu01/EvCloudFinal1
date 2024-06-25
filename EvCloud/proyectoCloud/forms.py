from django import forms
from proyectoCloud.models import Tareas

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tareas
        fields = ['titulo', 'descripcion', 'fecha_inicio', 'fecha_termino', 'prioridad']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'text', 'class': 'form-control', 'id': 'id_fecha_inicio'}),
            'fecha_termino': forms.DateInput(attrs={'type': 'text', 'class': 'form-control', 'id': 'id_fecha_termino'}),
            'prioridad': forms.Select(choices=[('Alta', 'Alta'), ('Media', 'Media'), ('Baja', 'Baja')], attrs={'class': 'form-control'}),
        }
