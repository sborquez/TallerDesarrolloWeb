
# Configurar la base de datos

Ya hemos visto dos capas de patrón MTV, la vista y el template. A continuación trabajaremos con la capa del Modelo.

## Configuración de PostgreSQL

Necesitamos crear una nueva base de datos para nuestra aplicación. Para esto debemos lanzar la herramienta de administración de PostgreSQL __Pg Admin4__.

Se nos abrirá el navegador, ingresamos con nuestro usuario y contraseña registrados al momento de instalar PostgreSQL.

Esta herramienta nos ayudará en visualizar nuestras bases de datos, ver nuestras tablas y los valores contenidos en ellas.

Debemos agregar un nuevo servidor. Hacemos clic en __Add New Server__. Los campos necesarios son:

*   Name: Nombre de nuestro servidor
*   Host name: En nuestro caso es _localhost_
*   Username y Password: Los usados al instalar PostgreSQL 

Luego creamos una nueva base de datos. Con clic derecho sobre nuestro nuevo servidor, _Create > Database_.

*   Database: Nombre de nuestra base de datos. Usaremos el mismo nombre de nuestra aplicación __WebApp__.

Una vez hecho esto, debemos configurar nuestra aplicación.

## Configurar nuestra aplicación

Django usa una sqlite como base de datos predeterminda, como usaremos la base de datos __postgreSQL__  debemos editar la configuración de nuestra aplicación en __/WebApp/WebApp/settings.py__, y editar el siguiente diccionario.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'WebApp',
        'USER': '[nombre de usuario]',
        'PASSWORD': '[contraseña]',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

Los valores de los atributos del diccionario deben coincidir con la confiración de nuestra base de datos.

Para probar nuestra configuración ejecutamos

```bash
>>>python manage.py migrate
```

<center><a href="https://github.com/sborquez/TallerDesarrolloWeb/blob/master/sesion2/Usando%20modelos.md">Siguiente</a></center>