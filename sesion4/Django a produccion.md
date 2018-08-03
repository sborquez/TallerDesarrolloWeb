# Django a producción

Una de las últimas fases de desarrollo de un producto de software es el paso a producción. Cuando llega el momento se debe tener en cuanta que la configuración de desarrollo es diferente, además se deben adoptar ciertas medidas de seguridad.

En esta sección nos enfocaremos en la configuración y las variables de entorno.

## Ocultando información

Cuando escribimos nuestro archivo de configuración dejamos expuestos datos importantes de seguridad.

```python

SECRET_KEY = '6-ob+6ww@e$%=fgvs_6!xbk@5x_!^xbydxrw=8#c73$1t==w1x'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'WebApp',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

Al hacer esto, cualquier individuo con acceso al código fuente de nuestra aplicación tendrá a disposición las credenciales para realizar algún tipo de ataque. Una buena forma de evitar esta exposición es utilizando las variables en entorno.

### Variables de entorno

Las variables de entorno son variables que dependen del sistema operativo y la configuración de este.

Para conocer las variables de entorno actualmente establecidas en nuestro sistema, solo es necesario abrir la consola de cmd e introducir el comando SET, se mostrarán todas las variables de entorno actuales junto con sus respectivos valores.

Si lo que se quiere ver es solo una variable usamos: echo %VARIABLE%

#### ¿Cómo crear una variable de entorno?

Puedes crear una variable de entorno mediante la línea de comandos, para eso utiliza el comando SETX de la siguiente forma: SETX VARIABLE VALOR (existe una alternativa a través de la interfaz gráfica)

### Usar las variables de entorno con python

Luego de haber crear una variable de entorno para los datos de la base de datos, la secret_key y para el modo debug podremos usarlas desde python. Para esto necesitamos el módulo os que nos entrega acceso a las funcionalidades del sistema operativo.

```python

import os

# SI no existe la variable, usamos cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag')

DEBUG = bool( os.environ.get('DJANGO_DEBUG', True) )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.enviroment("DJANGO_DB_NAME", "WebApp"),
        'USER': os.enviroment("DJANGO_DB_USER", 'postgres'),
        'PASSWORD': os.enviroment("DJANGO_DB_PASSWORD", 'postgres'),
        'HOST': os.enviroment("DJANGO_DB_HOST", '127.0.0.1'),
        'PORT': os.enviroment("DJANGO_DB_PORT", '5432'),
    }
}
```
