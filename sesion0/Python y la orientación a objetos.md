# Python

Django en un framework que utiliza como lenguaje de programación a  _Python_, el cual nos ofrece las siguientes caracteristicas para nuestro desarrollo.

Carácteristicas
+   Lenguaje interpretado y multiparadigma.
+   Sintaxis sencilla.
+   Gran variedad de módulos disponibles.
+   Gran disponibilidad de documentación.

## Python básico

A continuación veremos algunos conceptos básicos de _python_ los cuales utilizaremos durante el desarrollo de nuestro proyecto.

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

Para más detalles sobre la programacion básica de _python_ se encuentran disponibles los apuntes de Programación en Python: [progra.usm.cl](http://progra.usm.cl/Apuntes_del_curso.html)

## Clases y Objetos

La programación orientada a objetos [OOP](https://es.wikipedia.org/wiki/Programaci%C3%B3n_orientada_a_objetos) es un paradigma de la programación que busca organizar y representar objetos de la vida real describiendo sus caracteristicas y su comportamiento. Así, las clases poseen __atributos__ para describir a un objeto a traves de sus caracterisitas, como las columnas en una base de datos, y __métodos__, funciones que operan sobre los atributos de la clase, como las acciones que puede realizar un objeto en la realidad.

En terminos más formales, una __clase__ no es más que una plantilla de los atributos y métodos que un objeto posee, utilizada para definir como es el objeto y como se comportará. 

Por ejemplo, reprentar a una persona. Esta posee caracteristicas como su nombre y ciudad de nacimiento, también puede realizar acciones como saludar.

La siguiente clase es una abstracción de una persona:

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

Un __objeto__ es una instancia de una clase, una entidad independiente que posee atributos y realiza acciones definidos por la clase. Decir que son independientes significa que los atributos de un objeto no se comparten con otro.

En el siguiente ejemplo, se instancian dos objetos de tipo persona. Cada uno posee su nombre y ciuadad, al igual que pueden saludar, sin embargo un saldo de la persona_a será diferente al de la persona_b.

```python
persona_a = Persona("Juan", "La Serena")
persona_b = Persona("Ana", "Talcahuano")

persona_a.saludar()  # -> Hola, soy Juan y vengo de La Serena
persona_b.saludar()  # -> Hola, soy Ana y vengo de Talcahuano

print(persona_a.nombre == persona_b.nombre)  # Es Falso ya que Juan es diferente de Ana.

```

## Módulos útiles

Python posee una gran variedad de módulos por defecto, sin embargo la comunidad ha creado múltiples módulos para todo tipo de necesidades.

Algunos módulos incluidos con Python interesantes.
### CSV Para leer y escribir archivos csv
[Referencia](https://docs.python.org/3/library/csv.html)

### JSON Para codificar y decodificar json
[Referencia](https://docs.python.org/3/library/json.html)

### Datetime Para fechas y formatos de tiempo
[Referencia](https://docs.python.org/3/library/datetime.html)


Pip es un administrador de módulos aprovados por la comunidad, nos permite instalar, desinstalar y actualizar módulos, anaconda funciona sobre pip por lo que nos permite igualmente realizar estas acciones.

```python
conda install <nombre_del_modulo> # usando anaconda

pip install <nombre_del_modulo> # usando pip
``` 

Existen una gran variedad de módulos para diferentes propósitos. En este [repositorio](https://github.com/vinta/awesome-python) hay una lista que recolecta una gran cantidad de estos.


<center><a href="https://github.com/sborquez/TallerDesarrolloWeb/tree/master/sesion1/Qué%20es%20Django.md">Siguiente</a></center>