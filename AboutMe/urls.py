from django.urls import path
from AboutMe.views import about_me, contacto

app_name='AboutMe'

urlpatterns = [
    path('about_me/', about_me, name='about_me'),
    path('contacto/', contacto, name='contacto')
]
