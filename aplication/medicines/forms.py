from django import forms
from aplication.medicines.models import Medications

class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medications
        # Campos del formulario para el modelo de medicamentos
        fields = ['description', 'price', 'stock', 'is_active']  
             