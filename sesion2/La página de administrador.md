# La página de administrador

Django nos permite usar una página para administrar nuestros modelos. Esta se encuetra en __/admin/__. Pero es necesario configurarla antes de usarla.

## Creando un usuario administrador

Debemos ejecutar en el _conda prompt_ lo siguiente.

```python
python manage.py createsuperuser
```

Nos pedirá crear un usuario y contraseña.


## Registrando modelos

Debemos agregar los modelos a archivo __/WebApp/Blog/admin.py__

```python
from .models import Post, Blogger

# Register your models here.
admin.site.register(Post)
admin.site.register(Blogger)
```

## Usando la página de administrados

Podemos acceder al dashboard de administrador desde el la url __/admin__. Desde aquí podemos crear, ver y modificar los diferentes registros de nuestra base de datos.

<center><a href="https://github.com/sborquez/TallerDesarrolloWeb/blob/master/sesion2/M%C3%A1s%20sobre%20templates.md">Siguiente</a></center>
