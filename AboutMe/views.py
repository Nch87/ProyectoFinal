from django.shortcuts import render, redirect
from .models import AboutMe
from .forms import ContactoForm

def about_me(request):
    about_me = AboutMe.objects.first()
    return render(request, 'AboutMe/about_me.html', {'about_me': about_me})


def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = 'Gracias por contactarnos. Nos pondremos en contacto contigo a la brevedad.'
            return render(request, 'AppInicio/home.html', {'form': form, 'mensaje': mensaje})
    else:
        form = ContactoForm()
    
    return render(request, 'AboutMe/contacto.html', {'form': form})