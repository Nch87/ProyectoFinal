from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model

def image_upload_path(instance, filename):
    return 'adoption_images/{}/{}'.format(instance.id, filename)    

class Adopcion(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    raza = models.CharField(max_length=200,default='desconocida')
    edad = models.IntegerField(default=1)
    animal_info = models.TextField()
    imagen = models.ImageField(upload_to='adoption_images/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre 
    
class Comentario(models.Model):
    adopcion = models.ForeignKey(Adopcion, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor.username} en {self.adopcion.nombre}"   

class Ayuda(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Pet(models.Model):
    titulo = models.CharField(max_length=200)
    pet_info = models.TextField()
    contenido = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class Avatar(models.Model):
        imagen= models.ImageField(upload_to="avatars")
        user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank= True)
    
 
