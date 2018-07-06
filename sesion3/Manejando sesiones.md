# Manejando variables de sesión

Cuando trabajamos a través de la web por lo general utilizamos el protocolo HTTP, este es un protoco sin estado (stateless), esto quiere decir que existe una separación entre el cliente y el servidor. Esto implica que el servidor no mantiene información sobre lo que realizan los clientes. Sin embargo, esto puede ser implementado por nosotros, y gracias a Django esto resulta bastante sencillo. 

Django nos dispone de un framework para el manejo de sesiones. De esta forma el manejo de las _cookies_ y variables sesión quedarán a cargo del framework.

## Habilitar el uso de sessions

Podemos habilitar el uso de sesiones incluyendolo en nuestro archivo de configuración __WebApp/WebApp/settings.py__.

```python
INSTALLED_APPS = [
    ...
    'django.contrib.sessions',
    ...
]

MIDDLEWARE = [
    ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    ...
]
```

## Usando sessions

Al habilitar sessions tendremos acceso al _diccionario_ __session__. Este se encuentra disponible como un nuevo atributo de parámetro __request__ el cual utilizamos en nuestras _vistas_.

```python
def vista(request):
    ...
    request.session
    ...
```

Como cualquier diccionario de python podemos agregar, leer y modificar sus llaves y valores


```python
# Revisar si existe la llave
"language" in request.session

# Obteniendo un valor
lang = request.session["language"]

# Obteniendo un valor con default
lang = request.session.get("language", "en")

# Agregando llave y valor
request.session["color"] = "red"

# Modificar diccionario
request.session["color"] = "blue"


# Mostrar contenido del diccionario
request.session.values()    # lista de los valores
request.session.keys()      # lista de las llaves
request.session.items()     # lista de pares (llave, valor)

# Eliminar un valor
del request.session["color"]
```

Además _sessions_ nos entrega algunos métodos extras para el manejo de las sesiones.


```python
# Eliminar datos de la sesion
request.session.flush()

# Definir expiración de la sesión
# Expirar trás 5 minutos de inactividad
request.session.set_expiry(300) 

# Cantidad de segundos hasta que caduque la sesión.
request.session.get_expiry_age()

# Fecha de vencimiento de la sesión.
request.session.get_expiry_date()
```

La documentación completa de _sessions_ se encuentra [aquí](https://docs.djangoproject.com/en/1.10/topics/http/sessions/).


## Contador de visitas

Una aplicación sencilla de la API sessions es utilizar un contador de visitas de una página. Con esto se quiere saber cuantas veces el cliente ingresa a nuestro blog.

Para esto debemos modificar el archivo __WebApp/blog/views.py__.


```python
def index(request):

    visitas = request.session.get("visitas", 0)
    request.session["visitas"] = visitas + 1

    return render(request, "index.html", context={"visitas": visitas})
```

Luego de esto, tendremos que modificar el template correspondiente. __WebApp/blog/templates/index.html__


```html
{% extends "base.html" %}

{% block content %}
<h1>Blog Home</h1>

<p>Esta es la versión correspondiente la sesión 3</p>


<p><b>visitas:</b> {{ visitas }}</p>

{% endblock %}
```

<center><a href="https://github.com/sborquez/TallerDesarrolloWeb/blob/master/sesion3/Login%20y%20autenticación.md">Siguiente</a></center>