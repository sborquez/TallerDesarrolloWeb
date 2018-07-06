# Más sobre vistas y templates

## Usando referencias a url

A menudo utilizamos la etiqueta _a href_ de html para ir moviendonos a través de nuestra aplicación. Este etiqueta requiere del atributo _href_ el cual por lo general no queremos escribir manualmente. Django nos ayuda con esto usando la sentencia de los templates

    <a href="{% url 'nombre_de_url' %}">Go</a>

Para utilizarlo debemos modificar nuestras rutas en __WebApp/blog/url.py__ y agregarle a cada url el atributo __name__.


```python
urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^posts$", views.posts, name="posts"),
    url(r"^bloggers$", views.bloggers, name="bloggers"),
    ...
```

Luego de esta modificación podremos usar links como el siguiente.

```html
    <a href="{% url 'index' %}">Home</a>
```

## Usando archivos static

Django no ofrece archivos estáticos de manera predeterminada, debemos primero crear una carpeta en la raíz de nuestro proyecto.

    WebApp/public

Luego en el archivo de configuración __WebApp/WebApp/settings.py__ agregamos la siguiente sentencia.

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = ( os.path.join(BASE_DIR, "public"),)
```

Luego podemos crear nuestros archivos de estilo, creamos la carpeta __public/css__ y agregamos el siguiente archivo de estilo __style.css__ en ella.

```css
.sidebar-nav {
    margin-top: 20px;
    padding: 0;
    list-style: none;
    background-color: gainsboro
}
```

Para incluirlo en nuestras plantilla usaremos

    {% load static %}
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">


## Extendiendo templates


Por lo generar, las diferentas páginas que tiene una aplicación posee una estructura compartida, importan los mismos scripts y styles. Dado esto, podemos generar templates como base de otros templates.

Extender un template consiste en construir un template base que defina el estilo y layout de las páginas. Luego los templates especificos para cada página deben extender el contenido de la plantilla base. Para esto se utiliza siguiente sentencia.

    {% extends "template_base.html" %}

### Bloques de contendido

Extender un template consiste en definir _bloques de contenido_ en un template base y luego redefinirlos en los templates de cada página.

    {% block nombre_del_bloque %}
        <!-- Aqui agreagamos el contenido de la página-->
    {% endblock %}


### Creando un template base

Para nuestra aplicación usaremos el siguiente template base, lo llamaremos __base.html__.

```html
<!DOCTYPE html>
<html>
<head>
  
  {% block title %}<title>Blog</title>{% endblock %}
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  
  <!-- Importamos documentos de estilo-->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>


  <!-- Importamos documentos estaticos de estilo -->
  {% load static %}
  <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>

<body>

  <div class="container-fluid">

    <div class="row">
      <div class="col-sm-2">
      {% block sidebar %}
      <ul id="sidebar" class="sidebar-nav">
          <li><a href="{% url 'index' %}">Home</a></li>
          <li><a href="{% url 'posts'%}">Posts</a></li>
          <li><a href="{% url 'bloggers'%}">Bloggers</a></li>
      </ul>
     {% endblock %}
      </div>
      <div class="col-sm-10 ">
      {% block content %}{% endblock %}
      </div>
    </div>

  </div>
</body>
</html>
```

Como podemos apreciar, nuestro template base importa el framework de estilo __bootstrap__, además de crear tres bloques de contenido, uno para el titulo de la página, para una barra de navegación y para el contenido de la página.


### Extendiendo nuestro template index

Crearemos un nuevo template para nuestra página de inicio y lo llamaremos __index.html__.

Su contenido será el siguiente 

```html
{% extends "base.html" %}

{% block content %}
<h1>Blog Home</h1>

<p>Esta es la versión correspondiente la sesión 2</p>

{% endblock %}
```

Usamos __extends__ para llamar a nuestro template __base__.

Además redefinimos __{% block content %}__ con el contenido de nuestra página index.

Se debe seguir esta estructura para crear los diferentes templates para cada vista.


<center><a href="https://github.com/sborquez/TallerDesarrolloWeb/blob/master/sesion2/Pr%C3%A1ctica2.md">Práctica 2</a></center>
