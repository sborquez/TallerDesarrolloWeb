# Peticiones con variables

Cuando se realizan solicitudes usando URL, estas pueden contener variables. Un ejemplo seria si quiero ver un post en específico.

    /blogs/31

Pero, que sucede si el cliente quiere solicita otro blog como por ejemplo:

    /blogs/42

La lógica para renderizar ambas páginas es la misma, solo los datos cambian. Debemos programar nuestro controlador (urls.py) para que sea capáz de reaccionar a url genéricos.

Django dispone de esa facilidad [url dispacher](https://docs.djangoproject.com/en/2.0/topics/http/urls/).

## Agregar ruta

Agregaremos un controlador para ver un blog en particular en __WebApp/blog/urls.py__.

```python
urlpatterns = [
    url(r"^$", views.index),
    url(r"^post/(?P<blog_id>[0-9])$", views.blog)
]
```

Podemos usar distintos tipos o incluso expresiones regulares. [Aqui](https://docs.djangoproject.com/en/2.0/topics/http/urls/#path-converters)

## Agregar la vista

Antes de continuar, agregaremos esta variable al fichero __view.py__ para usar datos de prueba.

```python

usuarios = [
    {"id": 0, "nombre": "sebastian", "apellido": "borquez", "ciudad":"Valpariso"},
    {"id": 1, "nombre":"francisco", "apellido": "lara", "ciudad":"Santiago"}
]

blogs = [
    {"id": 0, "blogger":0, "titulo":"Primero Post", "contenido":"Este es el primer post."},
    {"id": 1, "blogger":0,"titulo": "Segundo Post", "contenido": "Este es el contenido del segundo post"},
    {"id": 2, "blogger":1, "titulo": "Tercer Post", "contenido": "Y Este es el tercer post del blog"}
]

```

Debemos agregar la nueva función para la vista.

```python
def blog(request, blog_id):
    try:
        blog_id = int(blog_id)
        return HttpResponse('<h1>{0}</h1><p>{1}</p>'.format(posts[blog_id]["titulo"], posts[blog_id]["contenido"]))
    except:
        return HttpResponse('<h1>No existe el blog</h1>')
```

# Renderizando Templates


Creamos una carpeta para nuestros templates y agregamos la siguente template

```html
<html>
<body>
    <h1>{{ titulo }}</h1>
    <p>{{ contenido }}</p>
</body>
</html>

```

Modificamos la vista para usar el template

```python
def blog(request, blog_id):
    try:
        blog_id = int(blog_id)
        return render(
            request,
            'post.html',
            context={'titulo':posts[blog_id]["titulo"], "contenido":posts[blog_id]["contenido"]},
        )
    except:
        return HttpResponse('<h1>No existe el blog</h1>')
```

