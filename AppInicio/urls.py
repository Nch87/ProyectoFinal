from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.contrib.admin.views.decorators import staff_member_required

app_name='AppInicio'

urlpatterns = [
  
   path('', home, name='home'),
   #Adopcion
   path('adopcion_lista/', adopcion_lista, name='adopcion_lista'),
   path("adopcion/<int:adopcion_id>/", adopcion_detalle, name="adopcion_detalle"),
   path('adopcion/nuevo/', adopcion_nuevo, name='adopcion_nuevo'),
   #Ayuda
   path('ayudas/', ayuda_detalle, name='ayuda_detalle'),
   path('ayuda_lista/', ayuda_lista, name='ayuda_lista'),
   path('ayuda_nueva/', ayuda_nueva, name='ayuda_nueva'),
   #Pet
   path('pet_detalle/<int:pk>/', pet_detalle, name='pet_detalle'),
   path('pet_lista/', pet_lista, name='pet_lista'),
   path('pet_nuevo/', pet_nuevo, name='pet_nuevo'),
   #Busqueda
   path("busqueda_adopcion/", busqueda_adopcion, name="busqueda_adopcion"),
   path("buscar/", buscar, name="buscar"),
   
    
    
 #LOGIN LOGOUT REGISTER
    
   path("login/", login_ingreso, name="login"),
   path("register/",register, name="register"),
   path("logout/",LogoutView.as_view(), name="logout"),
   path("editarPerfil/", editarPerfil, name="editarPerfil"),

]
