from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

app_name='AppInicio'

urlpatterns = [
  
   path('', home, name='home'),
   path('adopcion_detalle/', adopcion_detalle, name='adopcion_detalle'),
   path('adopcion_lista/', adopcion_lista, name='adopcion_lista'),
   path('ayuda_detalle/', ayuda_detalle, name='ayuda_detalle'),
   path('ayuda_lista/', ayuda_lista, name='ayuda_lista'),
   path('ayuda_nueva/', ayuda_nueva, name='ayuda_nueva'),
   path('pet_detalle/<int:pk>/', pet_detalle, name='pet_detalle'),
   path('pet_lista/', pet_lista, name='pet_lista'),
   path('pet_nuevo/', pet_nuevo, name='pet_nuevo'),
   path('adopcion/nuevo/', adopcion_nuevo, name='adopcion_nuevo'),
    
    
 #LOGIN LOGOUT REGISTER
    
   path("login/", login_ingreso, name="login"),
   path("register/",register, name="register"),
   path("logout/",LogoutView.as_view(), name="logout"),
   path("editarPerfil", editarPerfil, name="editarPerfil"),

]
