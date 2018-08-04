# Agregar diseño a las vistas

Luego de haber tenido un acercamiento con el framework, después de explorar templates y haber prototipado nuestro diseño en papel, es momento de implementarlo en nuestro proyecto de Django

## Modificando template base

### Agregar el framework

Como necesitamos acceder al framework desde todas nuestras vistas, debemos incorporarlo en nuestra plantilla base.

Quedando el inicio del template como

```html
<!DOCTYPE html>
<html>
<head>
  
  {% block title %}<title>Blog</title>{% endblock %}
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
  <!-- Para el uso de iconos -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <!-- Add additional CSS in static file -->
  {% load static %}
  <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body class= "w3-light-gray">
    ...
    ...
```

### Barra horizontal de navegación

Es uno de los elementos más comunes, consiste de una barra en la parte superior de la página que posee links para navegar por nuestro sitio web.

```html
    <!--Nav Bar-->
    <div class="w3-top">
        <div class="w3-bar w3-left-align w3-large w3-orange">
         <a class="w3-bar-item w3-button w3-hide-medium w3-hide-large w3-right w3-padding-large w3-hover-white w3-large w3-theme-d2" href="javascript:void(0);" onclick="openNav()"><i class="fa fa-bars"></i></a>
         <a href="{% url 'index' %}" class="w3-bar-item w3-button w3-padding-large w3-theme-d4"><i class="fa fa-home w3-margin-right"></i> Home</a>
         <a href="{%url 'posts'%}" class="w3-bar-item w3-button w3-padding-large w3-hover-white"><i class="fa fa-clipboard"></i></a>
         <a href="{%url 'bloggers'%}" class="w3-bar-item w3-button w3-padding-large w3-hover-white"><i class="fa fa-user"></i></a>
        </div>
       </div>
    <div>
```

### Login y Logout

Agregaremos a nuestra barra horizontal la opción para loguearse, además de mostrar las opciones de logout y link a la cuenta cuando inicie sesión.

```html
    <!--Nav Bar-->
    <div class="w3-top">
        <div class="w3-bar w3-left-align w3-large w3-orange">
         <a class="w3-bar-item w3-button w3-hide-medium w3-hide-large w3-right w3-padding-large w3-hover-white w3-large w3-theme-d2" href="javascript:void(0);" onclick="openNav()"><i class="fa fa-bars"></i></a>
         <a href="{% url 'index' %}" class="w3-bar-item w3-button w3-padding-large w3-theme-d4"><i class="fa fa-home w3-margin-right"></i> Home</a>
         <a href="{%url 'posts'%}" class="w3-bar-item w3-button w3-padding-large w3-hover-white"><i class="fa fa-clipboard"></i></a>
         <a href="{%url 'bloggers'%}" class="w3-bar-item w3-button w3-padding-large w3-hover-white"><i class="fa fa-user"></i></a>

          {% if user.is_authenticated %}
            <a href="{% url 'logout'%}?next={{request.path}}" class="w3-bar-item w3-button w3-right w3-padding-large w3-hover-white"><i class="fa fa-sign-out" aria-hidden="true"></i>Logout</a>
            <a href="{% url 'me' %}" class="w3-bar-item w3-button w3-right w3-padding-large w3-hover-white"> {{ user.get_username }}</a>
          {% else %}
            <a href="{% url 'login'%}?next={{request.path}}" class="w3-bar-item w3-button w3-right w3-padding-large w3-hover-white"><i class="fa fa-sign-in" aria-hidden="true"></i>Login</a>
          {% endif %}

        </div>
       </div>
    <div>
```

### Redefiniendo contenido

Ya no necesitaremos nuestro sidebar, por lo que se puede eliminar. Si cargamos la página en este estado veremos que la barra horizontal cubre el contenido. Para arreglar esto debemos primero envolver el contenido con un _container_ y luego agregar un margen al borde superior.

```html
    <div class="w3-container w3-content" style="max-width:1400px;margin-top:80px">
      {% block content %}{% endblock %}
    </div>
``` 

### Resumen

Llegado a este punto nuestro template base luce así

```html
<!DOCTYPE html>
<html>
<head>
  
  {% block title %}<title>Blog</title>{% endblock %}
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
  <!-- Para el uso de iconos -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <!-- Add additional CSS in static file -->
  {% load static %}
  <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>

<body class= "w3-light-gray">
    <!--Nav Bar-->
    <div class="w3-top">
        <div class="w3-bar w3-left-align w3-large w3-orange">
          <a href="{% url 'index' %}" class="w3-bar-item w3-button w3-padding-large w3-theme-d4"><i class="fa fa-home w3-margin-right"></i> Home</a>
          <a href="{%url 'posts'%}" class="w3-bar-item w3-button w3-padding-large w3-hover-white"><i class="fa fa-clipboard"></i></a>
          <a href="{%url 'bloggers'%}" class="w3-bar-item w3-button w3-padding-large w3-hover-white"><i class="fa fa-user"></i></a>


          {% if user.is_authenticated %}
            <a href="{% url 'logout'%}?next={{request.path}}" class="w3-bar-item w3-button w3-right w3-padding-large w3-hover-white"><i class="fa fa-sign-out" aria-hidden="true"></i>Logout</a>
            <a href="{% url 'me' %}" class="w3-bar-item w3-button w3-right w3-padding-large w3-hover-white"> {{ user.get_username }}</a>
          {% else %}
            <a href="{% url 'login'%}?next={{request.path}}" class="w3-bar-item w3-button w3-right w3-padding-large w3-hover-white"><i class="fa fa-sign-in" aria-hidden="true"></i>Login</a> 
          {% endif %} 
        </div>
    </div>

    <div class="w3-container w3-content" style="max-width:1400px;margin-top:80px">
      {% block content %}{% endblock %}
    </div>

  </div>
</body>
</html>
```

## Modificando templates de posts

El siguiente paso en nuestro diseño será modificar como se ven los posts. Comenzamos con la vista individual.

### Mostrar un post

Usaremos el contenedor __card__ que nos da un diseño acorde a un post.

```html
{% block content %}
<div class="w3-container w3-card w3-white w3-round w3-margin"><br>
    <span class="w3-right w3-opacity"><a href="/blog/blogger/{{blogger.id}}">{{blogger.nombre}} {{blogger.apellido}}</a></span>
    <h3>{{ titulo }}</h3><br>
    <hr class="w3-clear">
    <p>{{ contenido }}</p>
</div>
{% endblock %}
```

### Mostrar lista de posts

Usaremos la clase __w3-table-all__ para darle estilo a la tabla, además podemos usar __w3-center__ para centrar valores en la tabla.

```html
{% block content %}
    <div class="w3-container w3-white w3-round w3-margin">
        <h1>Posts</h1>
    <table class="w3-table-all">
            <tr class="w3-blue">
                <th>id</th><th>titulo</th><th>blogger</th><th class="w3-center">Editar</th><th class="w3-center">Eliminar</th>
            </tr>
            {%for element in posts%}
            <tr>
                <td>{{element.id}}</td>
                <td><a href="/blog/post/{{ element.pk }}">{{element.titulo}}</a></td>
                <td><a href="/blog/blogger/{{element.blogger.id}}">{{element.blogger.nombre}} {{element.blogger.apellido}}</a>  </td>
                <td class="w3-center"><a href="/blog/post/{{ element.pk }}/update/"><i class="fa fa-external-link-square" aria-hidden="true"></i></a></td>
                <td class="w3-center"><a href="/blog/post/{{ element.pk }}/delete/"><i class="fa fa-external-link-square" aria-hidden="true"></i></a></td>
            </tr>
            {% endfor %}
        </table>
        <br>
    </div>
{% endblock %}
```

Existe el problema de que, al utilizar pantallas pequeñas, la tabla no se verá correctamente. Para solucionarlo podemos agregarle la clase __w3-responsive__ sin embargo esto causa que no se vea bien con pantallas grandes. Tenemos otra opción, usar ambas, pero ocultar una dependiendo el tamaño de la pantalla.

```html
{% block content %}
    <div class="w3-container w3-white w3-round w3-margin">
        <h1>Posts</h1>
    <!-- para pantallas grandes-->
    <table class="w3-table-all w3-hide-small">
        <!-- mismo contenido -->
    </table>
    <!-- para pantallas pequeñas -->
    <table class="w3-table-all w3-responsive w3-hide-large w3-hide-medium">
        <!-- mismo contenido -->
    </table>
    <br>
    </div>
{% endblock %}

```

### Formulario para un post



```html

{% block content %}
<form action="" method="post" style="width:412px"  class="w3-container  w3-card-4 w3-light-grey w3-text-blue w3-margin">
    {% csrf_token %}
    <h2> Post </h2>
    <div class="w3-row w3-section">
      <h4>Titulo</h4>
      {{ form.titulo }}
    </div>
    <div class="w3-row w3-section">
      <h4>Contenido</h4>
      <div class="w3-rest">
        {{ form.contenido }}
      </div>
    </div>
    <div>
      <input class="w3-button w3-block w3-section w3-blue w3-ripple w3-padding" type="submit" value="Enviar" />
      <input type="hidden" name="next" value="{{ next }}" />
    </div>
  </form>
{% endblock %}
```



### Confirmar eliminar post

Las clases __w3-panel__ son perfectos para mostrar mensajes importantes como la confirmación para eliminar una instancia.

```html
<div class="w3-panel w3-pale-red">
    <h3>Atención!</h3>

    <p>Está a punto de eliminar el post: {{ post }}</p>
    <form action="" method="POST">
      {% csrf_token %}
        <input class="w3-btn w3-round-large w3-white w3-hover-red" type="submit" action="" value="Eliminar"/>
    </form>
    <br>
</div>
```

### Formulario para iniciar sesión

En este caso debemos aparte de modificar el formulario, agregar alertas para los errores.

```html
{% if form.errors %}
  <div class="w3-panel w3-red w3-display-container">
    <span onclick="this.parentElement.style.display='none'"
    class="w3-button w3-red w3-large w3-display-topright">&times;</span>
    <h3>Atención!</h3>
    <p>El usuario y/o contraseña no coinciden, prueba de nuevo.</p>
  </div>
{% endif %}

{% if next %}
    {% if user.is_authenticated %}
    <div class="w3-panel w3-red w3-display-container">
        <span onclick="this.parentElement.style.display='none'"
        class="w3-button w3-red w3-large w3-display-topright">&times;</span>
        <h3>Atención!</h3>
        <p>Tu cuenta no posee los permisos necesarios para acceder a la página.</p>
      </div>
    {% endif %}
{% endif %}
```

Y para el formulario

```html
<div class="w3-row">
  
  <form method="post" action="{% url 'login' %}" class="w3-container  w3-card-4 w3-light-grey w3-text-blue w3-margin w3-third w3-center">
    {% csrf_token %}
    <h2 class="w3-center">Bienvenido</h2>
    <div class="w3-row w3-section">
      <div class="w3-col" style="width:50px"><i class="w3-xxlarge fa fa-user"></i></div>
      {{ form.username }}
    </div>
    <div class="w3-row w3-section">
      <div class="w3-col" style="width:50px"><i class="fa fa-key" aria-hidden="true"></i></div>
      <div class="w3-rest">
        {{ form.password }}
      </div>
    </div>
    <div>
      <input class="w3-button w3-block w3-section w3-blue w3-ripple w3-padding" type="submit" value="login" />
      <input type="hidden" name="next" value="{{ next }}" />
    </div>
  </form>
</div>
```

### Practica

Implementar los estilos para las vistas faltantes