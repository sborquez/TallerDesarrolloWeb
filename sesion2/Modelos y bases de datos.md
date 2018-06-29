


### Configurar la base de datos

Antes de seguir avanzando en nuestro proyecto es necesario configurar la base de datos que se va a utilizar.

En nuestro caso usaremos la base de datos __postgreSQL__, debemos editar la configuración de nuestro proyecto __/WebApp/WebApp/settings.py__

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '[nombre de la base de datos]',
        'USER': '[nombre de usuario]',
        'PASSWORD': '[contraseña]',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

Los valores de los atributos del diccionario deben coincidir con la confuración de nuestra base de datos.