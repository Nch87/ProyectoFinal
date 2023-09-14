from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required 


def home(request):
    return render(request,"AppInicio/home.html")
    
def register(request):
       if request.method=="POST":
           form=RegistroUserForm(request.POST)
           if form.is_valid():
               info=form.cleaned_data
               nombre_user=info["username"]
               form.save()
               return render(request, "AppInicio/home.html", {"mensaje":f"Usuario {nombre_user} Creado Correctamente"})
           else:
                return render(request, "AppInicio/register.html", {"form":form, "mensaje":"Datos Invalidos"})
       else:
           form=RegistroUserForm()
           return render(request, "AppInicio/register.html", {"form":form})

def login_ingreso(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            user=info["username"]
            clave=info["password"]
            usuario=authenticate(username=user, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppInicio/home.html", {"mensaje":f"Usuario {user} Ingreso Correctamente"})        
            else:
                return render(request, "AppInicio/login.html", {"form":form, "mensaje":"Datos Invalidos"})
        else:
            return render(request, "AppInicio/login.html", {"form":form, "mensaje":"Datos Invalidos"})
    else:
        form=AuthenticationForm()
        return render(request, "AppInicio/login.html", {"form":form})

@login_required
def editarPerfil(request):
    usuario=request.user
    
    if request.method=="POST":
       form=UserEditForm(request.POST)
       if form.is_valid():
          info=form.cleaned_data
          usuario.email=info["email"]
          usuario.password1=info["password1"]
          usuario.password2=info["password2"]
          usuario.first_name=info["first_name"]
          usuario.last_name=info["last_name"]
          usuario.save()
          return render(request, "AppInicio/home.html", {"mensaje":f"Usuario {usuario.username} Editado Correctamente"})           
       else:
          return render(request, "AppInicio/editarPerfil.html", {"form": form, "nombreusuario":usuario.username, "mensaje": "Datos Invalidos"})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "AppInicio/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})


def adopcion_lista(request):
    adopciones = Adopcion.objects.all()
    return render(request, 'AppInicio/adopcion_lista.html', {'adopciones': adopciones})


def adopcion_detalle(request):
    adopciones = Adopcion.objects.all()
    return render(request, 'AppInicio/adopcion_detalle.html', {'adopciones': adopciones})

@login_required
def adopcion_nuevo(request):
    if request.method == "POST":
        form = AdopcionForm(request.POST, request.FILES)
        if form.is_valid():
            adopcion = form.save(commit=False)
            adopcion.autor = request.user
            adopcion.save()
            return redirect("AppInicio:home")
    else:
        form = AdopcionForm()
    return render(request, 'AppInicio/adopcion_nuevo.html', {'form': form})

@login_required
def ayuda_lista(request):
    ayuda = Ayuda.objects.all()
    return render(request, 'AppInicio/ayuda_lista.html', {'ayuda': ayuda})

@login_required
def ayuda_detalle(request, pk):
    ayuda = get_object_or_404(Ayuda, pk=pk)
    return render(request, 'AppInicio/ayuda_detalle.html', {'ayuda': ayuda})

@login_required
def ayuda_nueva(request):
    if request.method == "POST":
        form = AyudaForm(request.POST)
        if form.is_valid():
            ayuda = form.save(commit=False)
            ayuda.save()
            return redirect('AppInicio/ayuda_detalle', pk=ayuda.pk)
    else:
        form = AyudaForm()
    return render(request, 'AppInicio/ayuda_edit.html', {'form': form})

@login_required
def pet_lista(request):
    pets = Pet.objects.all()
    return render(request, 'AppInicio/pet_lista.html', {'pets': pets})

@login_required
def pet_detalle(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'AppInicio/pet_detalle.html', {'pet': pet})

@login_required
def pet_nuevo(request):
    if request.method == "POST":
        form = PetForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.save()
            return redirect('AppInicio/pet_detalle', pk=pet.pk)
    else:
        form = PetForm()
    return render(request, 'AppInicio/pet_edit.html', {'form': form})