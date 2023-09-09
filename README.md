# ProyectoFinal
Proyecto Final Natalia Chazarreta
Este es el repositorio para el Proyecto Final del curso de Python
Descripción
Este proyecto es una aplicación web para una organización sin fines de lucro que se dedica a ayudar a los animales. La aplicación permite a los usuarios ver información sobre animales disponibles para adopción, publicar comentarios en publicaciones de blog y obtener información sobre cómo ayudar a la organización.

# Funcionalidades
Ver una lista de animales disponibles para adopción.
Ver detalles sobre un animal en particular, incluyendo una imagen y una descripción.
Publicar comentarios en publicaciones de blog.
Ver una lista de publicaciones de blog.
Ver detalles sobre una publicación de blog en particular, incluyendo comentarios.
Ver información sobre cómo ayudar a la organización.

# Modelos
Post
Atributos:
title: campo CharField con una longitud máxima de 100 caracteres para almacenar el título del post.
content: campo TextField para almacenar el contenido del post.
date_posted: campo DateTimeField con auto_now_add=True para registrar la fecha y hora en que se creó el post.
author: campo ForeignKey que establece una relación con el modelo User para almacenar el autor del post.
Comment
Atributos:
post: campo ForeignKey que establece una relación con el modelo Post para almacenar el post al que pertenece el comentario.
author: campo ForeignKey que establece una relación con el modelo User para almacenar el autor del comentario.
content: campo TextField para almacenar el contenido del comentario.
date_posted: campo DateTimeField con auto_now_add=True para registrar la fecha y hora en que se creó el comentario.
Adopcion
Atributos:
titulo: campo CharField con una longitud máxima de 200 caracteres para almacenar el título de la adopción.
imagen: campo ImageField para almacenar la imagen relacionada con la adopción.
animal_info: campo TextField para almacenar información sobre el animal disponible para adopción.
contenido: campo TextField para almacenar detalles adicionales sobre la adopción.
pub_date: campo DateTimeField con auto_now_add=True para registrar la fecha y hora en que se creó la adopción.
Ayuda
Atributos:
titulo: campo CharField con una longitud máxima de 200 caracteres para almacenar el título de la ayuda.
contenido: campo TextField para almacenar información sobre cómo brindar ayuda.
pub_date: campo DateTimeField con auto_now_add=True para registrar la fecha y hora en que se creó la ayuda.
Pet
Atributos:
titulo: campo CharField con una longitud máxima de 200 caracteres para almacenar el título de la mascota.
pet_info: campo TextField para almacenar información sobre la mascota.
contenido: campo TextField para almacenar detalles adicionales sobre la mascota.
pub_date: campo DateTimeField con auto_now_add=True para registrar la fecha y hora en que se creó la mascota.
# Formularios
LoginForm
Campos:
email: campo EmailField para ingresar el correo electrónico del usuario.
password1: campo CharField con widget de PasswordInput para ingresar la contraseña del usuario.
password2: campo CharField con widget de PasswordInput para confirmar la contraseña.
UserEditForm
Campos:
email: campo EmailField para ingresar el correo electrónico del usuario.
password1: campo CharField con widget de PasswordInput para ingresar la nueva contraseña del usuario.
password2: campo CharField con widget de PasswordInput para confirmar la nueva contraseña.
first_name: campo CharField para modificar el nombre del usuario.
last_name: campo CharField para modificar el apellido del usuario.
# Vistas
Adopcion_nuevo: vista para crear una nueva adopción.
Adopcion_detalle: vista para ver los detalles de una adopción específica.
Ayuda_lista: vista para mostrar una lista de ayudas disponibles.
Ayuda_detalle: vista para ver los detalles de una ayuda específica.
Pet_lista: vista para mostrar una lista de mascotas disponibles.
Pet_detalle: vista para ver los detalles de una mascota específica.
# Este proyecto utiliza las siguientes bibliotecas y recursos:
Bootstrap 5
Font Awesome 5
Imágenes de animales 

