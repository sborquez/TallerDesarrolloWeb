# Login y autenticación

Django además nos ofrece un sistema de [auteticación y permisos](https://docs.djangoproject.com/en/2.0/topics/auth/default/) construido sobre el framework de sesiones. Esto nos permitirá crear usuario, asignarle permisos y iniciar sesión en nuestra aplicación. 

## Habilitar el uso de authentication


Podemos habilitar el uso de authentication incluyendolo en nuestro archivo de configuración __WebApp/WebApp/settings.py__.

```python
INSTALLED_APPS = [
    ...
    'django.contrib.auth', 
    'django.contrib.contenttypes',
    ....

MIDDLEWARE = [
    ...
    'django.contrib.sessions.middleware.SessionMiddleware', 
    ...
    'django.contrib.auth.middleware.AuthenticationMiddleware', 
    ....
```

## Creando usuarios y grupos

Anteriormente ya creamos un usuario, el superusuario para la página de _admin_ es un usuario el cual posee todos los permisos. Pero podemos agregar más usuario usando la página de administrador.

Para esto ingresamos a [página de admin](http://127.0.0.1:8000/admin/), hacemos clic en [+add](http://127.0.0.1:8000/admin/auth/group/add/) al lado de _groups_.

Luego creamos un grupo de prueba con el nombre de __Blog Members__ y guardamos los cambios con __SAVE__.


Ahora debemos crear un usuario de prueba, nuevamente desde la [página de admin](http://127.0.0.1:8000/admin/), hacemos clic en [+add](http://127.0.0.1:8000/admin/auth/user/add/) al lado de _users_.

Luego rellenamos con un nombre y contraseña, guardamos con __SAVE__. Esto nos llevará a la página del usuario. Aquí debemos agregarlo al grupo __Blog Members__ y guardamos los cambion son __SAVE__.

## Agregando nuevas vistas

A continuación debemos configurar las vistas y templates para las funciones de autenticación. Django nos ofrece ya las vistas, pero no los templates.

### Agregando urls

Para agregar las urls para los sitios de autenticación debemos agregar lo siguiente en el archivo de _urls_ de nuestro proyecto __WebApp/WebApp/urls.py__.

```python
urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
```

Con esto se encontrarán disponibles los siguientes urls:
*   login: accounts/login/
*   logout: accounts/logout/
*   password_change: accounts/password_change/$
*   password_change_done: accounts/password_change/done/$
*   password_reset: accounts/password_reset/$
*   password_reset_done: accounts/password_reset/done/$
*   password_reset_confirm: accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$
*   password_reset_complete: accounts/reset/done/$

### Carpeta de templates

Los templates para la autenticación no se encuentran en la misma carpeta que nuestros templates de la aplicación. Debemos crear una nueva carpeta en la raíz de nuestro proyecto (junto a WebApp, public y blog) llamada __templates__, dentro de esta creamos la carpeta __registration__.

Añadimos la carpeta en nuestro archivo de configuración __WebApp/WebApp/settings.py__.

```python
TEMPLATES = [
    {
        ...
        'DIRS': ['./templates',],
        'APP_DIRS': True,
        ...
```

Luego tendremos que crear los siguentes _templates_ en __WebApp/templates/registration__.

*   login.html
*   logged_out.html
*   password_reset_complete.html
*   password_reset_confirm.html
*   password_reset_done.html
*   password_reset_email.html
*   password_reset_form.html

### Login

El contenido del template de _login_ es el siguiente.

```html
{% extends "base.html" %}

{% block content %}

{% if form.errors %}
<p>El usuario y/o contraseña no coinciden, prueba de nuevo.</p>
{% endif %}

{% if next %}
    {% if user.is_authenticated %}
    <p>Tu cuenta no posee los permisos necesarios para acceder a la página.</p>
    {% else %}
    <p>Login</p>
    {% endif %}
{% endif %}

<form method="post" action="{% url 'login' %}">
{% csrf_token %}

<div>
  <td>{{ form.username.label_tag }}</td>
  <td>{{ form.username }}</td>
</div>
<div>
  <td>{{ form.password.label_tag }}</td>
  <td>{{ form.password }}</td>
</div>

<div>
  <input type="submit" value="login" />
  <input type="hidden" name="next" value="{{ next }}" />
</div>
</form>

<p><a href="{% url 'password_reset' %}">Olvidó su password?</a></p>

{% endblock %}
```

Luego de un login exitoso no redireccionará a la url designada por la siguiente variable en __WebApp/WebApp/settings.py__.

```python
# redireccionar al index
LOGIN_REDIRECT_URL = '/'
```

### Logout

```html
{% extends "base.html" %}

{% block content %}
<p>Logged out!</p>  

<a href="{% url 'login'%}">Login again.</a>
{% endblock %}
```

Podemos probar nuestro _login_ con la url [login](http://localhost:8000/accounts/login/) y luego [logout](http://localhost:8000/accounts/logout/).

### Password reset

Para esta vista es necesario crear varios templates, tanto para elegir la nueva contraseña, confirmación y email que se envia.

### password_reset_complete.html
```html
    {% extends "base.html" %}
    {% block content %}

    <h1>Contraseña cambiada!</h1>
    <p><a href="{% url 'login' %}">login</a></p>

    {% endblock %}
```
### password_reset_confirm.html
```html

{% extends "base.html" %}

{% block content %}

    {% if validlink %}
        <p>Ingrese contraseña nueva.</p>
        <form action="" method="post">
            <div style="display:none">
                <input type="hidden" value="{{ csrf_token }}" name="csrfmiddlewaretoken">
            </div>
            <table>
                <tr>
                    <td>{{ form.new_password1.errors }}
                        <label for="id_new_password1">Nueva contraseña:</label></td>
                    <td>{{ form.new_password1 }}</td>
                </tr>
                <tr>
                    <td>{{ form.new_password2.errors }}
                        <label for="id_new_password2">Confirmar contraseña:</label></td>
                    <td>{{ form.new_password2 }}</td>
                </tr>
                <tr>
                    <td></td>
                    <td><input type="submit" value="Change my password" /></td>
                </tr>
            </table>
        </form>
    {% else %}
        <h1>Password reset failed</h1>
    {% endif %}

{% endblock %}
```
### password_reset_done.html
```html
{% extends "base.html" %}
{% block content %}
    <p>Hemos enviado a tu email las intrucciones para cambiar tu contrañesa </p>
{% endblock %}
```
### password_reset_email.html
```html
Alguien pidio un cambio de contraseña usando este email: {{ email }}. Siga el link debajo.
{{ protocol}}://{{ domain }}{% url 'password_reset_confirm' uidb64=uid token=tok
```
### password_reset_form.html
```html
{% extends "base.html" %}
{% block content %}

<form action="" method="post">{% csrf_token %}
    {% if form.email.errors %} {{ form.email.errors }} {% endif %}
        <p>{{ form.email }}</p> 
    <input type="submit" class="btn btn-default btn-lg" value="Reset password" />
</form>

{% endblock %}

```



### Mostrar informaciona a usuario autenticados

#### A través del template

A continuación modificaremos nuestro template base (__WebApp/blog/templates/base.html__) para mostrar el nombre del usuario autenticado o el acceso al login si aún no se ha iniciado sesión.

Para esto utilizaremos la variable de contexto  __user__ disponible en los templates, _user_ está predefinido por Django y posee dos métodos que nos permitirán identificar al usuario.

```html
    {{ user.is_authenticated }} <!-- boolean determina si el usuario es legible-->
    {{ user.get_username }} <!-- Es el nombre del usuario-->
```

Además podemos utilizar la siguiente sentencia para renderizar ciertas partes del template solo si el usuario está autenticado.

```html
    {% if user.is_authenticated %}
        ...
    {% else %}
        ...
    {% endif %} 
```

Modificamos nuestra template base y agregamos lo siguiente.

```html
    {% block sidebar %}
        <ul id="sidebar" class="sidebar-nav">
        ...
        {% if user.is_authenticated %}
          <li>User: {{ user.get_username }}</li>
          <li><a href="{% url 'logout'%}?next={{request.path}}">Logout</a></li>   
        {% else %}
          <li><a href="{% url 'login'%}?next={{request.path}}">Login</a></li>   
        {% endif %} 
        ...
        </ul>
    {% endblock %}
```

Podemos ver dos sentencias nuevas, _next_ y _request.path_.

El primero, _next_ se encarga de redireccionar al usuario luego de un login exitoso. En cuento a _request.path_, este almacena el valor de la url actual.

Entonces, luego de un _login_ o _logout_ exitoso, se redirecciona a la página actual.

#### A través de la vista

Otra forma en que podemos ocultar información a usuario no autenticados es modificando la función de la vista con un [__decorador__](https://wiki.python.org/moin/PythonDecorators#What_is_a_Decorator) de Django.

```python
from django.contrib.auth.decorators import login_required

@login_required
def funcion_de_vista(request):
    ...
```

Para nuestro ejemplo, crearemos una nueva vista llamada __me__ la cual solo los usarios que iniciaron sesión pueden acceder.

__WebApp/blog/views.py__
```python
from django.contrib.auth.decorators import login_required

@login_required
def me(request):
    return render(request, "me.html")
```
__WebApp/blog/urls.py__
```python
urlpatterns = [
    ...
    url(r"^me$", views.me, name="me")
]
```

__WebApp/blog/templates/me.html__
```html
{% extends "base.html" %}

{% block content %}
<h1> Usuario: {{ user.get_username }}</h1>
{% endblock content %}
```

__WebApp/blog/templates/base.html__
```html
<!--Modificamos esta linea para agregar un link a me-->
 <li>User: <a href="{% url 'me' %}"> {{ user.get_username }}</a></li>
```

Podemos ver que si queremos acceder a [http://localhost:8000/blog/me](http://localhost:8000/blog/me) sin haber iniciado sesión, este nos redireccionará a la página de login. 