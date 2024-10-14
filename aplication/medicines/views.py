from django.urls import reverse_lazy
from aplication.medicines.forms import MedicationForm
from aplication.medicines.models import Medications
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

class medicament_ListView(LoginRequiredMixin, ListView):
    model = Medications
    template_name = 'medicines/list_medicament.html'
    context_object_name = 'medicament_list'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Medical'
        context['title1'] = 'Sistema Medico Online'
        return context
    
class Medicament_CreateView(LoginRequiredMixin, CreateView):
    model = Medications
    form_class = MedicationForm
    template_name = 'medicines/form_medicament.html'
    success_url = reverse_lazy('medicines:medicament_list')  # Redirecciona a la lista de medicamentos
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Medical'
        context['title1'] = 'Crear nuevo medicamento'
        context['title3'] = 'Grabar medicamento'
        return context
    
    def form_valid(self, form): 
        # Asigna el usuario autenticado al campo 'user' del modelo Medications
        form.instance.user = self.request.user
        return super().form_valid(form)

class Medicament_UpdateView(LoginRequiredMixin, UpdateView):
    model = Medications
    form_class = MedicationForm
    template_name = 'medicines/form_medicament.html'
    success_url = reverse_lazy('medicines:medicament_list') #Redireccion a la lista de doctores
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Medical'
        context['title1'] = 'Editar medicamento'
        return context
    
    def form_valid(self, form): 
        # Asigna el usuario autenticado al campo 'user' del modelo Medications
        form.instance.user = self.request.user
        return super().form_valid(form)

class medicament_DeleteView(LoginRequiredMixin, DeleteView):
    model = Medications
    template_name = 'medicines/delete_medicament.html'
    success_url = reverse_lazy('medicines:medicament_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar'
        context['title1'] = 'Eliminar Medicamento'
        context['medication'] = self.object  
        return context  


