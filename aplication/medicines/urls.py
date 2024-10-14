from django.urls import path
from aplication.medicines import views
 
app_name= 'medicines' # define un espacio de nombre para la aplicacion

urlpatterns = [
  path('medicament_list/', views.medicament_ListView.as_view(),name="medicament_list"),
  path('medicament_create/', views.Medicament_CreateView.as_view(),name="medicament_create"),
  path('medicament_update/<int:pk>/', views.Medicament_UpdateView.as_view(),name='medicament_update'),
  path('medicament_delete/<int:pk>/', views.medicament_DeleteView.as_view(),name='medicament_delete'),
]

