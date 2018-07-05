# Python

Usaremos _Python_ para escribir la lógica que ocurre del lado del servidor de nuestra aplicación web. 

Carácteristicas
+   Lenguaje interpretado y multiparadigma.
+   Sintaxis sencilla.
+   Gran variedad de módulos disponibles.
+   Gran disponibilidad de documentación.

## Python básico

```python
# incluir modulos
import math

# diccionarios
post1 = {
    "titulo" : "Primer post".
    "contenido" : "Contenido del post"
}

# listas
gastos = [20, 10, 30, 20, 0, 10]

usuario = {
    "nombre": "Sebastian",
    "apellido":"Borquez",
    "carrera": 73,
    "posts" : [post1]
    "gastos" = gastos
}


#funciones
def elevar(numeros, potencia):
    for i,numero in enumerate(numeros):
        print("{0}: {1}".format(i,math.pow(numero, potencia)))

```


Apuntes de Programación en Python: [progra.usm.cl](http://progra.usm.cl/Apuntes_del_curso.html)

## Clases y Objetos

La programación orientada a objetos [OOP](https://es.wikipedia.org/wiki/Programaci%C3%B3n_orientada_a_objetos) es un paradigma de la programación que busca organizar y representar objetos de la vida real describiendo sus caracteristicas y su comportamiento. Así, las clases poseen __atributos__ y __métodos__.

Una __clase__ no es más que una plantilla de los atributos y métodos que un objeto posee. Por ejemplo, reprentar a una persona podemos usar la siguiente clase.

```python

class Persona(object):
    # __init__ se ejecuta al instanciar un objeto 
    def __init__(self, nombre, ciudad):
        # self siempre es el primer argumento
        # self.<nombre> son los atributos
        self.nombre = nombre
        self.ciudad = ciudad
    def saludar(self):
        print("Hola, soy {0} y vengo de {1}".format(nombre, ciudad))
``` 

Un __objeto__ se crea al instanciar una clase, los atributos de cada objeto son independientes entre ellos 

```python
persona_a = Persona("Juan", "La Serena")
persona_b = Persona("Ana", "Talcahuano")

persona_a.saludar()
persona_b.saludar()

print(persona_a.nombre == persona_b.nombre)

``` 



## Módulos útiles

Algunos módulos incluidos con Python interesantes.

### CSV Para leer y escribir archivos csv
[Referencia](https://docs.python.org/3/library/csv.html)

### JSON Para codificar y decodificar json
[Referencia](https://docs.python.org/3/library/json.html)

### Datetime Para fechas y formatos de tiempo
[Referencia](https://docs.python.org/3/library/datetime.html)


Para instalar nuevos módulos podemos usar anaconda o pip

Existen una gran variedad de módulos para diferentes propósitos. En este [repositorio](https://github.com/vinta/awesome-python) hay una lista que recolecta una gran cantidad de estos. 

```python
conda install <nombre_del_modulo> # usando anaconda

pip install <nombre_del_modulo> # usando pip
``` 

<center><a href="https://github.com/sborquez/TallerDesarrolloWeb/tree/master/sesion1/Qué%20es%20Django.md">Siguiente</a></center>