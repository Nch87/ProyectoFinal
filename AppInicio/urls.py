from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
  #LOGIN LOGOUT REGISTER
    
    path('login/', login_ingreso, name='login'),
    path('register/',register, name='register'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('editarPerfil', editarPerfil, name='editarPerfil'),
    
    
    path('adopcion_detalle/<int:pk>/', adopcion_detalle, name='adopcion_detalle'),
    path('adopcion_lista/', adopcion_lista, name='adopcion_lista'),
    path('adopcion_nuevo/', adopcion_nuevo, name='adopcion_nuevo'),
    path('ayuda_detalle/<int:pk>/', adopcion_detalle, name='adopcion_detalle'),
    path('ayuda_lista/', ayuda_lista, name='ayuda_lista'),
    path('ayuda_nueva/', ayuda_nueva, name='ayuda_nueva'),
    path('pet_detalle/<int:pk>/', pet_detalle, name='pet_detalle'),
    path('pet_lista/', pet_lista, name='pet_lista'),
    path('pet_nuevo/', pet_nuevo, name='pet_nuevo'),
    
    
]
