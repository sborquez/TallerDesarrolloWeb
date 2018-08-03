# Preparación del ambiente de desarrollo

## Anaconda

[Anaconda](https://www.anaconda.com/distribution/) es una herramienta de desarrollo de aplicaciones en python.  Nos permitirá manejar las dependecias de nuestra aplicación, asi como instalar nuevos módulos y crear 'ambientes virtuales'.

### Instalación 

Descargar el instalador de **Python 3.6** correspondiente a su sistema operativo usando este [link](https://www.anaconda.com/download/).

Luego de la instalación las aplicaciones que nos intererán son:
*   Anaconda Navigator: GUI para creación de ambientes virtuales, instalación  de módulos y herramientas.
*   Anaconda Prompt: CLI para instalar usar los ambientes virtuales y ejecutar aplicaciones.

### Creando un ambiente virtual

Un ambiente virtual es una configuración independiente de nuestro sistema operativo, lo utilizamos para evitar colisiones de versiones entre las dependencias instaladas en nuestro computador y las requeridas por nuestro proyecto.

Tenemos dos métodos para crear un ambiente virtual.

#### Usando Anaconda Navigator

    1   Environments->Create
    2   Name: WebApp Python: 3.6
    3   Para agregar modulos
        Mostrar: Not installed
        Buscar: django


#### Usando Anaconda Prompt

```python
conda create -n WebApp python=3.6

source activate WebApp  # Linux y Mac
activate WebApp         # Windows

conda install django
```

#### Probar instalación

Podemos probar si nuestra instalación fué exitosa desde Anaconda Promp

```python
source activate WebApp  # Linux y Mac
activate WebApp         # Windows
python
```
La salida debe ser similar a lo siguiente

```python
Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more 
information.
>>>
```
Finalmente importamos el modulo de django

```python
>>> import django
```

Si no se genera ningún error, nuestro ambiente de desarrollo está configurado correctamente.

## Editor de textos

Recomiendo usar uno de estos editores de textos. A ambos se le pueden agregar nuevas funcionalidades y soporte para lenguajes.

1. [Visual Studio Code](https://code.visualstudio.com/)
2. [Sublime text 3](https://www.sublimetext.com/)

## Bases de datos

Django soporta cuatro bases de datos importantes (PostgreSQL, MySQL, Oracle y SQLite). Además Python cuenta con módulos para otras bases de datos como MongoDB.

Para el desarrollo de este taller utilizaremos PostgreSQL, puede descargar desde su [página oficial](https://www.postgresql.org/download/).

Sin embargo, Django nos proporciona flexibilidad para intercambiar la base de datos gracias al uso del patrón Object-Relational Mapper [ORM](https://es.wikipedia.org/wiki/Mapeo_objeto-relacional)


<center><a href="https://github.com/sborquez/TallerDesarrolloWeb/tree/master/sesion0/Los%20lenguajes%20para%20construir%20páginas%20web.md">Siguiente</a></center>