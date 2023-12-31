from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.contrib import messages


#Inicio
def home(request):
    return render(request,"AppInicio/home.html")


# Registro y Perfil    
def register(request):
       if request.method=="POST":
           form=RegistroUserForm(request.POST)
           if form.is_valid():
               info=form.cleaned_data
               nombre_user=info["username"]
               form.save()
               return render(request, "AppInicio/home.html", {"mensaje":f"Usuario {nombre_user} Creado Correctamente, Bienvenido a nuestra Comunidad"})
           else:
                return render(request, "AppInicio/register.html", {"form":form, "mensaje":"Datos Invalidos"})
       else:
           form=RegistroUserForm()
           return render(request, "AppInicio/register.html", {"form":form})
    
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


# ADOPCIONES

def adopcion_lista(request):
    adopciones = Adopcion.objects.all()
    return render(request, 'AppInicio/adopcion_lista.html', {'adopciones': adopciones})

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

@user_passes_test(lambda u: u.is_authenticated, login_url='AppInicio:register')
@login_required
def adopcion_detalle(request, adopcion_id):
    adopcion = get_object_or_404(Adopcion, id=adopcion_id)
    comentarios = adopcion.comentarios.order_by('-pub_date')
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.adopcion = adopcion
            comentario.autor = request.user
            comentario.save()
            return redirect("AppInicio:adopcion_detalle", adopcion_id=adopcion.id)
    else:
        form = ComentarioForm()
    return render(request, "AppInicio/adopcion_detalle.html", {"adopcion": adopcion, "comentarios": comentarios, "form": form})


#AYUDAS

@user_passes_test(lambda u: u.is_authenticated, login_url='AppInicio:register')
@login_required
def ayuda_lista(request):
    if request.method == 'POST':
        form = AyudaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "AppInicio/home.html", {"mensaje":" Muchas Gracias por tu Colaboracion"}) 
    else:
        form = AyudaForm()
    return render(request, "AppInicio/ayuda_lista.html", {'form': form})

@login_required
def ayuda_detalle(request):
    ayudas = Ayuda.objects.all()
    return render(request, "AppInicio/ayuda_detalle.html", {'ayudas': ayudas})

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


# Mascotas


def pet_lista(request):
    pets = Pet.objects.all()
    return render(request, 'AppInicio/pet_lista.html', {'pets': pets})

@login_required
def pet_nuevo(request):
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.autor = request.user
            pet.save()
            return redirect("AppInicio:home")
    else:
        form = PetForm()
    return render(request, 'AppInicio/pet_nuevo.html', {'form': form})

# Login

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

# Busqueda Adopcion 

@login_required
def busqueda_adopcion(request):
    return render(request,"AppInicio/busqueda_adopcion.html")

@login_required
def buscar(request):
    raza=request.GET["raza"]
    if raza!="":
        adopcion=Adopcion.objects.filter(raza__icontains=raza)
        return render(request, "AppInicio/resultadoBusqueda.html",{"adopcion":adopcion})
    else:
        return render(request,"AppInicio/busqueda_adopcion.html", {"mensaje":"No se ingresaron Datos"})   
    

# Editar Publicacion Adopcion

@login_required
def editarAdopcion(request, id):
    adopcion = get_object_or_404(Adopcion, id=id)
    
    if adopcion.autor != request.user:
        return HttpResponse("No tienes permiso para editar esta publicación.")
    
    if request.method == 'POST':
        formulario = AdopcionForm(request.POST, request.FILES, instance=adopcion)
        if formulario.is_valid():
            adopcion = formulario.save(commit=False)
            adopcion.autor = request.user
            adopcion.save()
            return redirect('AppInicio:adopcion_detalle', adopcion_id=id)
    else:
        formulario = AdopcionForm(instance=adopcion)
    
    return render(request, 'AppInicio/editarAdopcion.html', {'formulario': formulario, 'adopcion': adopcion})


# Eliminar Publicacion Adopcion

@login_required
def eliminarAdopcion(request, id):
    adopcion = get_object_or_404(Adopcion, id=id)
    if adopcion.autor != request.user:
        return HttpResponse("No tienes permiso para eliminar esta publicación.")
    adopcion.delete()
    messages.success(request, 'La publicación de adopción ha sido eliminada exitosamente.')
    formulario_adopcion = AdopcionForm()
    adopciones = Adopcion.objects.all()
    return render(request, "AppInicio/adopcion_lista.html", {"formulario": formulario_adopcion, "adopcion": adopciones})



     
