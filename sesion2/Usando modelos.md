# Usando modelos

Django nos permite acceder y administrar laos datos de nuestra aplicación a través del uso de objetos lladamos modelos los cuales son independientes de la base de datos elegida. Los modelos definen la estructura de los datos almacenados, incluidos los tipos de campo y los atributos de cada campo, como su tamaño máximo, valores predeterminados, lista de selección de opciones, texto de ayuda para la documentación, texto de etiqueta para formularios, etc.

Rara vez tendremos que utilizar sentencias de SQL para acceder a la base de datos, Django se encargará de realizar las _queries_ necesarias.

## Usando django.models

### Definición

Los modelos son definidos en archivos __models.py__, se definen implementando subclases de la clase __django.db.models.Model__. Debemos seguir la siguiente estructura.

```python
from django.db import models

class MiModelo(models.Model):
    """
    Aqui va una pequeña documentación sobre el modelo.
    """

    # Campos
    nombre_de_atributo = models.CharField(max_length=20, help_text="Texto de ayuda")
    ...

    # Metadata
    class Meta: 
        ordering = ["-nombre_de_atributo"]

    # Métodos
    # Agregamos nuestros métodos extras
```

Los tipos de campos pueden ser:

*   CharField: Campo de texto
*   TextField: Campo de texto, usado para textos largos.
*   IntegerField: Para números.
*   DateField:  Para fechas
*   EmailField: Para correos electrónicos.
*   AutoField:  Para números autoingrementables,
*   ForeignKey: Se usa para le lado de "uno" en relaciones _uno a muchos_.
*   ManyToManyField: Para espeficicar relaciones _muchos a muchos_. 

Aquí una [lista](https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types) completa de tipos de campos y aquí una [lista](https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-options) de sus opciones.

### Creando nuevos registros

Para crear nuevos registros en nuestra base de datos debemos primero instanciar un nuevo objeto de nuestro modelo.

```python
nueva_registro = MiModelo(nombre_de_atributo="mi primer registro")
```

Podemos modificar sus atributos:

```python
nueva_registro.nombre_de_atributo = "Mi Primer Registro!"
```

Luego para almacenarlo en la base de datos usamos el método _save()_.

```python
nueva_registro.save()
```

### Haciendo consultas

Para realizar consultas en la base de datos debemos realizarla a travéz de nuestro modelo usando _modelo.objects_. Podemos obtener todos los registros utilizando lo siguiente.

```python
todos_los_registros = MiModelo.objects.all()
```

Tambien podemos filtrar nuestras busquedas, en este caso podemo usar _filter_.

```python
registros = MiModelo.filter(nombre_de_atributo__contains='Mi')
```

O quizás buscar un registro en especifico con get y __exact.

```python
un_registros = MiModelo.objects.get(nombre_de_atributo__exact="Mi Primer Registro!")
```

Para seguir leyendo, [aquí](https://docs.djangoproject.com/en/1.10/ref/models/querysets/) la referencia a los QuerySet de Django.


## Modelos del blog

<img src="https://raw.githubusercontent.com/sborquez/TallerDesarrolloWeb/master/sesion2/ClassDiagram.png">

El diagrama de clases de nuestra aplicación es bastante simple, solo necesitamos dos modelos.

### Modelo Blogger

Consiste de tres campos de texto o __CharField__ y un campo para el correo.

```python
class Blogger(models.Model):
    """
    Modelo que representa a un blogger
    """
    nombre = models.CharField(max_length=20, blank=False, null=False)
    apellido = models.CharField(max_length=20, blank=False, null=False)
    ciudad = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField()


    def __str__(self):
        return self.nombre + "_" + self.apellido 

```

### Modelo Post

Un post posee título __CharField__, contenido __TextField__, una fecha de publicación __TimeField__ con el atributo _auto_now_add_ para que se genere al momento de crear la instancia, finalmente necesita relacionarse con la tabla __Blogger__ usando una __ForeignKey__.

```python
class Post(models.Model):
    """
    Modelo que representa a una publicación.
    """
    titulo = models.CharField(max_length=120, blank=False, null=False)
    contenido = models.TextField(blank=False, null=False)
    publicacion = models.TimeField(auto_now_add=True)   
    blogger = models.ForeignKey('Blogger', related_name='blogger', on_delete=models.CASCADE, null=False)

    class Meta:
        ordering = ["publicacion"]

    def __str__(self):
        return self.titulo
```

## Modificando las vistas

Para terminar nuestra implementación de los modelos es neceario modificar nuestras vistas para que ultilicen a los modelos.

Comenzamos importando los modelos a nuestro archivo de vistas __views.py__.

```python
# Importamos los modelos
from .models import Post, Blogger
```

### Bloggers

Comenzamos con el más sencillo, basta con consultar por todos los objetos.

```python
def bloggers(request):
    _bloggers = Blogger.objects.all()
    return render(request, "bloggers.html", context={"bloggers":_bloggers})
```

### Posts

Al igual que Bloggers, basta con consultar por todos los objetos.

```python
def posts(request):
    posts_plus = Post.objects.all()
    return render(request, "posts.html", context={"posts":posts_plus})

```

### Blogger

En el caso de Blogger, usaremos _get_ y *__exact* para obtener el blogger especifico. Luego usaremos _filter_ para acceder a sus posts.

```python
def blogger(request, blogger_id):
    try:
        blogger_id = int(blogger_id)
        _blogger = Blogger.objects.get(id__exact=blogger_id)
        _posts = Post.objects.filter(blogger__id = blogger_id)
        return render(
            request,
            'blogger.html',
            context={ \
                "nombre":_blogger.nombre,
                "apellido":_blogger.apellido,
                "ciudad":_blogger.ciudad,
                "posts": _posts}
        )
    except Exception as err:
        print(err)
        return HttpResponse('<h1>No existe el post</h1>')
```

### Post

En el caso de Post, usaremos _get_ y *__exact* para obtener el post especifico.

```python
def post(request, post_id):
    try:
        post_id = int(post_id)
        _post = Post.objects.get(id__exact=post_id)
        return render(
            request,
            'post.html',
            context={\
                "titulo":_post.titulo,
                "contenido":_post.contenido,
                "blogger": _post.blogger
            },
        )
    except:
        return HttpResponse('<h1>No existe el post</h1>')
```

## Guardando cambios

Para efectuar nuestros cambios de los modelos en la base de datos debemos ejecutar

```bash
>>python manage.py makemigrations
>>python manage.py migrate
```

<center><a href="https://github.com/sborquez/TallerDesarrolloWeb/blob/master/sesion2/La%20p%C3%A1gina%20de%20administrador.md">Siguiente</a></center>