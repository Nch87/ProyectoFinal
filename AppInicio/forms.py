from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserEditForm(UserCreationForm):
    email=forms.EmailField(label="Email Usuario")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)  
    first_name=forms.CharField(label="Modificar Nombre")
    last_name=forms.CharField(label="Modificar Apellido")
    
    class Meta:
        model=User
        fields=["username", "email", "password1", "password2", "first_name", "last_name"]
        help_texts= {k:"" for k in fields}  
        
class RegistroUserForm(UserCreationForm):
    email=forms.EmailField(label="Email")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts= {k:"" for k in fields} 

class AdopcionForm(forms.ModelForm):
    class Meta:
        model = Adopcion
        fields = ('autor','nombre', 'raza', 'edad', 'animal_info', 'imagen')

class AyudaForm(forms.ModelForm):
    class Meta:
        model = Ayuda
        fields = ('titulo', 'contenido')
        
class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('titulo', 'pet_info', 'contenido')        
                          