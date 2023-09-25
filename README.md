# ProyectoFinal
## Proyecto Final Natalia Chazarreta
Este es el repositorio para el Proyecto Final del curso de Python

## Descripción
- La aplicación es un es un sitio web que permite a los usuarios registrarse, editar su perfil, publicar solicitudes de adopción y solicitudes de ayuda, así como contactar al propietario del sitio web.

- El sitio web utiliza varios modelos de Django para almacenar información de los usuarios, incluidos el nombre de usuario, la dirección de correo electrónico, la contraseña y la información de perfil. También hay modelos para almacenar publicaciones de adopción y solicitudes de ayuda.

- Para registrar un nuevo usuario, el sitio web utiliza un formulario de registro que valida la información del usuario antes de crear una nueva cuenta. Los usuarios existentes pueden editar su perfil utilizando un formulario de edición que valida los cambios antes de actualizar la información del usuario en la base de datos.

- Los usuarios pueden publicar solicitudes de adopción utilizando un formulario que incluye información sobre el animal. Las publicaciones se almacenan en la base de datos y se muestran en una lista en la página principal del sitio web.

- Los usuarios también pueden publicar solicitudes de ayuda utilizando un formulario que incluye información sobre el tipo de ayuda que podrian aportar. Las solicitudes se almacenan en la base de datos y se muestran en una lista en la página principal del sitio web unicamente a los usuarios ADMIN.

- Finalmente, los usuarios pueden contactar al propietario del sitio web a través de un formulario de contacto. Los mensajes enviados a través del formulario se validan antes de ser guardados en la base de datos. Si el mensaje se guarda correctamente, se muestra un mensaje de confirmación en la misma página.

- En resumen, la aplicación es una plataforma en línea para conectar a los usuarios interesados en adoptar animales o brindar ayuda a otros usuarios que necesiten asistencia, todo mientras proporciona una forma fácil y segura para que los usuarios se comuniquen con el propietario del sitio web.

## Funcionalidades Principales
- Registro y autenticación de usuarios
- Edición de perfil de usuario
- Publicación de solicitudes de adopción de animales
- Publicación de solicitudes de ayuda
- Visualización de una lista de publicaciones de adopción y solicitudes de ayuda
- Comunicación con el propietario del sitio web a través de un formulario de contacto

## Modelos

### Adopcion
- Este modelo representa una publicación de adopción de animales. 
Atributos:
- autor: una relación de clave foránea (ForeignKey) con el modelo User, que indica el usuario que creó la publicación.
- nombre: un campo de texto (CharField) que representa el nombre del animal.
- raza: un campo de texto (CharField) que representa la raza del animal. Tiene un valor predeterminado de 'desconocida'.
- edad: un campo de texto (CharField) que representa la edad del animal. Tiene un valor predeterminado de '1'.
- animal_info: un campo de texto largo (TextField) que contiene información adicional sobre el animal.
- imagen: un campo de imagen (ImageField) que representa la imagen del animal.
- fecha_creacion: un campo de fecha y hora (DateTimeField) que indica cuándo se creó la publicación.
### Ayuda
- Este modelo representa una solicitud de ayuda
Atributos:
-nombre: un campo de texto (CharField) que representa el nombre del solicitante.
- email: un campo de correo electrónico (EmailField) que representa la dirección de correo electrónico del solicitante.
- telefono: un campo de texto (CharField) que representa el número de teléfono del solicitante.
- mensaje: un campo de texto largo (TextField) que contiene el mensaje de ayuda.
- fecha: un campo de fecha y hora (DateTimeField) que indica cuándo se creó la solicitud.
### Pet
- Este modelo representa una publicación sobre mascotas
Atributos:
- titulo: un campo de texto (CharField) que representa el título de la publicación.
- autor: una relación de clave foránea (ForeignKey) con el modelo User, que indica el usuario que creó la publicación. Tiene un valor predeterminado de 1.
- pet_info: un campo de texto largo (TextField) que contiene información adicional sobre la mascota.
- imagen: un campo de imagen (ImageField) que representa la imagen de la mascota.
- fecha_creacion: un campo de fecha y hora (DateTimeField) que indica cuándo se creó la publicación.
### AboutMe
- Este modelo representa información personal sobre el usuario del sitio web.
Atributos:
- nombre: un campo de texto (CharField) que representa el nombre del usuario.
- descripcion: un campo de texto largo (TextField) que contiene una descripción o información adicional sobre el usuario.
- imagen: un campo de imagen (ImageField) que representa la imagen del usuario. Este campo es opcional, ya que se le ha asignado los parámetros blank=True, null=True, lo que significa que puede estar vacío.
### Contacto
Este modelo representa un formulario de contacto para que los visitantes del sitio web puedan enviar mensajes. 
Atributos:
- nombre: un campo de texto (CharField) que representa el nombre del remitente del mensaje.
- email: un campo de correo electrónico (EmailField) que representa la dirección de correo electrónico del remitente.
- mensaje: un campo de texto largo (TextField) que contiene el mensaje enviado por el remitente.
- Ambos modelos tienen un método __str__ que devuelve una representación legible del objeto en forma de cadena. Esto es útil cuando se necesita mostrar o imprimir los objetos en el código.
### Comentario
- Este modelo representa un comentario en una publicación de adopción. 
Atributos:
- adopcion: una relación de clave foránea (ForeignKey) con el modelo Adopcion, que indica la publicación a la que se refiere el comentario.
- autor: una relación de clave foránea (ForeignKey) con el modelo User, que indica el usuario que escribió el comentario.
- contenido: un campo de texto largo (TextField) que contiene el contenido del comentario.
- pub_date: un campo de fecha y hora (DateTimeField) que indica cuándo se publicó el comentario.
  
## Formularios

### Formulario UserEditForm
- Este formulario se utiliza para editar la información de un usuario existente. Tiene los siguientes campos:
- email: un campo de correo electrónico (EmailField) que representa la dirección de correo electrónico del usuario.
- password1: un campo de contraseña (CharField) que representa la nueva contraseña del usuario.
- password2: un campo de confirmación de contraseña (CharField) que se utiliza para confirmar la nueva contraseña del usuario.
- first_name: un campo de texto (CharField) que representa el nombre del usuario.
- last_name: un campo de texto (CharField) que representa el apellido del usuario.

### Formulario RegistroUserForm
- Este formulario se utiliza para registrar un nuevo usuario en el sitio web. Tiene los siguientes campos:
- email: un campo de correo electrónico (EmailField) que representa la dirección de correo electrónico del usuario.
- password1: un campo de contraseña (CharField) que representa la contraseña del usuario.
- password2: un campo de confirmación de contraseña (CharField) que se utiliza para confirmar la contraseña del usuario.

### Formulario AdopcionForm
- Este formulario se utiliza para crear una nueva publicación de adopción. Tiene los siguientes campos:
- autor: un campo de selección (Select) que permite al usuario seleccionar su nombre de usuario como autor de la publicación.
- nombre: un campo de texto (CharField) que representa el nombre del animal.
- raza: un campo de texto (CharField) que representa la raza del animal.
- edad: un campo de texto (CharField) que representa la edad del animal.
- animal_info: un campo de texto largo (TextField) que contiene información adicional sobre el animal.
- imagen: un campo de imagen (ImageField) que representa la imagen del animal.

### Formulario AyudaForm
- Este formulario se utiliza para enviar una solicitud de ayuda. Tiene los siguientes campos:
- nombre: un campo de texto (CharField) que representa el nombre del solicitante.
- email: un campo de correo electrónico (EmailField) que representa la dirección de correo electrónico del solicitante.
- telefono: un campo de texto (CharField) que representa el número de teléfono del solicitante.
- mensaje: un campo de texto largo (TextField) que contiene el mensaje de ayuda.

### Formulario PetForm
- Este formulario se utiliza para crear una nueva publicación sobre una mascota. Tiene los siguientes campos:
- titulo: un campo de texto (CharField) que representa el título de la publicación.
- autor: un campo de selección (Select) que permite al usuario seleccionar su nombre de usuario como autor de la publicación.
- pet_info: un campo de texto largo (TextField) que contiene información adicional sobre la mascota.
- imagen: un campo de imagen (ImageField) que representa la imagen de la mascota.

### Formulario ComentarioForm
- Este formulario se utiliza para agregar comentarios a una publicación de adopción. Tiene los siguientes campos:
- contenido: un campo de texto largo (TextField) que contiene el contenido del comentario.

### Formulario ContactoForm
- Este formulario se utiliza para enviar mensajes a través del formulario de contacto. Tiene los siguientes campos:
- nombre: un campo de texto (CharField) que representa el nombre del remitente del mensaje.
- email: un campo de correo electrónico (EmailField) que representa la dirección de correo electrónico del remitente.
- mensaje: un campo de texto largo (TextField) que contiene el mensaje enviado por el remitente.

## Vistas

### Vista home
Esta vista se utiliza para mostrar la página de inicio del sitio web.

### Vista register
Esta vista se utiliza para registrar un nuevo usuario en el sitio web. Si el método de solicitud es POST, el formulario de registro se valida y se crea un nuevo usuario. Si el formulario no es válido, se muestra un mensaje de error y se vuelve a mostrar el formulario. Si el método de solicitud es GET, se muestra el formulario de registro.

### Vista editarPerfil
Esta vista se utiliza para editar la información del perfil de un usuario existente. Si el método de solicitud es POST, el formulario de edición se valida y se actualiza la información del usuario. Si el formulario no es válido, se muestra un mensaje de error y se vuelve a mostrar el formulario. Si el método de solicitud es GET, se muestra el formulario de edición con los datos actuales del usuario.

### Vista adopcion_lista
Esta vista se utiliza para mostrar una lista de publicaciones de adopción existentes.

### Vista adopcion_nuevo
Esta vista se utiliza para crear una nueva publicación de adopción. Si el método de solicitud es POST, el formulario de creación se valida y se crea una nueva publicación. Si el formulario no es válido, se muestra un mensaje de error y se vuelve a mostrar el formulario. Si el método de solicitud es GET, se muestra el formulario de creación.

### Vista adopcion_detalle
Esta vista se utiliza para mostrar los detalles de una publicación de adopción existente y permitir a los usuarios agregar comentarios a la publicación.

### Vista ayuda_lista
Esta vista se utiliza para mostrar una lista de solicitudes de ayuda existentes. Si el método de solicitud es POST, el formulario de creación se valida y se crea una nueva solicitud. Si el formulario no es válido, se muestra un mensaje de error y se vuelve a mostrar el formulario. Si el método de solicitud es GET, se muestra el formulario de creación.

### Vista ayuda_detalle
Esta vista se utiliza para mostrar una lista de solicitudes de ayuda existentes.

### Vista ayuda_nueva
Esta vista se utiliza para crear una nueva solicitud de ayuda. Si el método de solicitud es POST, el formulario de creación se valida y se crea una nueva solicitud. Si el formulario no es válido, se muestra un mensaje de error y se vuelve a mostrar el formulario. Si el método de solicitud es GET, se muestra el formulario de creación.

### Vista pet_lista
Esta vista se utiliza para mostrar una lista de mascotas existentes.

### Vista pet_nuevo
Esta vista se utiliza para crear una nueva mascota. Si el método de solicitud es POST, el formulario de creación se valida y se crea una nueva mascota. Si el formulario no es válido, se muestra un mensaje de error y se vuelve a mostrar el formulario. Si el método de solicitud es GET, se muestra el formulario de creación.

### Vista login_ingreso
Esta vista se utiliza para permitir a los usuarios iniciar sesión en el sitio web. Si el método de solicitud es POST, los datos del usuario se validan y si son correctos, el usuario inicia sesión en el sitio web. Si los datos no son válidos, se muestra un mensaje de error y se vuelve a mostrar el formulario. Si el método de solicitud es GET, se muestra el formulario de inicio de sesión.

### Vista busqueda_adopcion
Esta vista se utiliza para mostrar la página que permite a los usuarios buscar publicaciones de adopción por raza.

### Vista buscar
Esta vista se utiliza para buscar publicaciones de adopción por raza y mostrar los resultados en una página separada.

### Vista About_me
Esta vista se utiliza para mostrar información sobre el propietario del sitio web. Esta vista utiliza el modelo "AboutMe" para obtener la información que se mostrará y la devuelve en la plantilla "about_me.html". Si no hay información disponible en el modelo "AboutMe", se mostrará una página en blanco.

### Vista contacto
Esta vista se utiliza para permitir que los usuarios envíen un mensaje de contacto al propietario del sitio web. Si el método de solicitud es POST, el formulario de contacto se valida y se guarda el mensaje. Si el formulario no es válido, se muestra un mensaje de error y se vuelve a mostrar el formulario. Si el método de solicitud es GET, se muestra el formulario de contacto vacío. Esta vista utiliza el formulario "ContactoForm" y la plantilla "contacto.html". Si el mensaje se guarda correctamente, se muestra un mensaje de confirmación en la misma página.

## Este proyecto utiliza las siguientes bibliotecas y recursos:
- Bootstrap 5
- Imágenes de animales
## Link de Presentacion del Pryecto Final
- https://screenapp.io/app/#/shared/3d546e62-3658-4f80-9453-d0ac0d11c076

