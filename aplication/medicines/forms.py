from django import forms
from aplication.core.models import Medications

class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medications
        # Campos del formulario para el modelo de medicamentos
        fields = ['description', 'price', 'stock', 'is_active']  # Reemplazando campos del doctor por los del medicamento
             