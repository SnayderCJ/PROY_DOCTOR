from django.urls import path
from aplication.medicines import views
 
app_name= 'medicines' # define un espacio de nombre para la aplicacion

urlpatterns = [
  # ruta principal
  path('', views.home,name='medicina'),
  # rutas de doctores
  path('doctor_list/', views.doctor_List,name="doctor_list"),
  path('doctor_create/', views.doctor_create,name="doctor_create"),
  path('doctor_update/<int:id>/', views.doctor_update,name='doctor_update'),
  path('doctor_delete/<int:id>/', views.doctor_delete,name='doctor_delete'),
  
]

