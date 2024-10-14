from django.urls import reverse_lazy
from django.shortcuts import render
from aplication.core.forms import DoctorForm
from aplication.core.models import Doctor
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

         
def home(request):
   data={"title":"Medical","title1":"Sistema Medico Online"}
   #return HttpResponse("<h1>Pantalla de Inicio</h1>")
   #return JsonResponse(data)
   return render(request,'core/home.html',data)

class doctor_ListView(ListView):
    model = Doctor
    template_name = 'core/doctor/list.html'
    context_object_name = 'doctor_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Medical'
        context['title1'] = 'Sistema Medico Online'
        return context

class Doctor_CreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'core/doctor/form.html'
    success_url = reverse_lazy('core:doctor_list') #Redireccion a la lista de doctores
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Medical'
        context['title1'] = 'Crear un nuevo doctor'
        return context
    
class Doctor_UpdateView(UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'core/doctor/form.html'
    success_url = reverse_lazy('core:doctor_list') # Redireccion a la lista de doctores
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Medical'
        context['title1'] = 'Editar doctor'
        return context
    
class doctor_DeleteView(DeleteView):
    model = Doctor
    template_name = 'core/doctor/delete.html'
    success_url = reverse_lazy('core:doctor_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar'
        context['title1'] = 'Eliminar doctor'
        return context




