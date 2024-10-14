from django.urls import path
from aplication.core import views
from django.conf.urls.static import static
from django.conf import settings
 
app_name='core' 

urlpatterns = [
  # ruta principal
  path('', views.home,name='home'),

  path('doctor_list/', views.doctor_ListView.as_view(),name="doctor_list"),
  path('doctor_create/', views.Doctor_CreateView.as_view(),name="doctor_create"),
  path('doctor_update/<int:pk>/', views.Doctor_UpdateView.as_view(),name='doctor_update'),
  path('doctor_delete/<int:pk>/', views.doctor_DeleteView.as_view(),name='doctor_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)