from django.urls import path
from aplication.security import views
from django.conf.urls.static import static
from django.conf import settings
 
app_name= 'security' # define un espacio de nombre para la aplicacion

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.siging, name='signin'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)