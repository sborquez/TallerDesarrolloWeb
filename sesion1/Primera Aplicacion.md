# Primera aplicación

## Iniciar un nuevo proyecto

Un proyecto es un conjunto de diferentes aplicaciones que correrán en nuestro servidor.

Desde la Anaconda Prompt ejecutamos la siguiente línea.

```bash
django-admin startproject WebApp
```
Esto nos generará los siguentes archivos en nuestro directorio.

    WebApp/
        manage.py
        WebApp/
            __init__.py
            settings.py
            urls.py
            wsgi.py

* settings.py contiene todos los ajustes del sitio. Es donde registramos todas las aplicaciones que creamos, la localización de nuestros ficheros estáticos, los detalles de configuración de la base de datos, etc.
* urls.py define los mapeos url-vistas. A pesar de que éste podría contener todo el código del mapeo url, es más común delegar algo del mapeo a las propias aplicaciones, como verás más tarde.
* wsgi.py se usa para ayudar a la aplicación Django a comunicarse con el servidor web. 

* manage.py se usa para crear aplicaciones, trabajar con bases de datos y empezar el desarrollo del servidor web.


Podemos probar que el correcto funcionamiento de nuestro proyecto ejecutando


## Crear una nueva aplicación

Para crear una nueva aplicación usamos la siguiente linea de comando desde el directorio WebApp

```bash
cd WebApp
python manage.py startapp blog
```


    WebApp/
        manage.py
        WebApp/
        blog/
            __init__.py
            admin.py
            apps.py
            models.py
            tests.py
            views.py
            migrations/ 

### Registrar la aplicación

Para poder utilizar la nueva aplicación esta debe estar registrada en el proyecto.

Abrimos __WebApp/WebApp/settings.py__ y agreagamos lo siguiente

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Agregamos esta linea
    'blog.apps.blogConfig', 
]
```

La nueva linea especifica el objeto de configuración de la aplicación (CatalogConfig) que se generó para en __/WebApp/blog/apps.py__.

Podemos probar el funcionamieto de nuestra aplicación ejecutando

```bash
python manage.py runserver
```

## Conectar vistas a urls

La administración de urls puede modificarse con la variable __urlpatterns__ en __/WebApp/WebApp/urls.py__


urlpatterns consiste en una lista de funciones _path(url, view)_ la cual conecta una url con su vista correspondiente.

Para agregar nuevas urls para nuestra aplicación debemos agregar lo siguiente

```python
from django.urls import include

urlpatterns += [
    path('blog/', include('blog.urls')),
]
``` 

Debemos ahora la URL raíz a nuestra aplicación

```python
from django.views.generic import RedirectView

urlpatterns += [
    path('', RedirectView.as_view(url='/blog/', permanent=True)),
]
``` 


Para que nuestra aplicación pueda servir ficheros estáticos como css o images debemos agregar lo siguiente

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
``` 

Además, debemos agregar la siguiente linea en __WebApp/WebApp/settings.py__ y crear una nueva carpeta llamada __public__ en __WebApp__.

```python
STATIC_ROOT = "/public/"
``` 

Finalmente debemos configurar las url de nuestra aplicación, agregamos el archivo __blog/urls.py__ con el siguiente contenido.

```python
from django.conf.urls import url

from . import views


urlpatterns = [

]
``` 

### Agregando vistas

El primer paso para agregar una nueva vista es crear una función que maneje la lógica de la operación.

Una vista es una función que procesa una consulta HTTP, trae datos desde la base de datos cuando los necesita, genera una página HTML renderizando estos datos unando una plantilla HTML, y luego retorna el HTML en una respuesta HTTP para ser mostrada al usuario.

Las vistas van en el fichero __views.py__

Crearemos una nueva vista para la página de inicio. Para agregamos a las vistas el siguiente código.

```python
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello World!')

```
El parámetro de HttpResponse es un objeto HTML, por lo que podemos usar todas sus etiquetas o escribir directamente la página en html, por ejemplo.

```python
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello World!</h1><p>Es servidor está corriendo</p>')

```

Ahora falta conectar la vista con las urls en __urls.py__

```python
from . import views
from django.urls import path
from django.urls import include
from django.conf.urls import url

urlpatterns = [
    url(r"^$", views.index),
]
```

Podemos probar lanzando nuestro servidor con:

```bash
python manage.py runserver
```

Deberiamos poder ver en nuestro navegador un "_Hello World!_".

