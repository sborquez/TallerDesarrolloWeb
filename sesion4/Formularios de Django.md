# Formularios de Django

Django provee una serie de herramieta para ayudarnos a completar las siguientes tareas necesarias para manipular los datos ingresados por un usuario.

1. Renderizar un formulario por defecto, con sus valores predeterminados.
2. Recibir las información solicitada y mostrarla en el formulario en caso de ser necesario.
3. Limpiar y validar el input, es decir, detectar inputs maliciosos, identificar si el input es del tipo pedido.
4. Informar en caso de que los datos fueron erroneos.
5. Realizar las operaciones necesarias en caso de un input válido.
6. Redireccionar finalmente al usuario a una vista.

## Clase Form

La clase Form es fundamental para la manipulación de entradas en nuestra aplicación. Especifica tanto la forma del formulario, tipos de datos, labels, valores predefinidos y placeholders. También podemos crear métodos para la validación de inputs, renderizar templates, entre otros.

### Declarar un formulario

Comenzaremos creando un nuevo archivo llamado __forms.py__ en la aplicación: __WebApp/blog/forms.py__

Lo primero que se debe hacer es importar el módulo.

```python
from django import forms
```

El siguiente paso es declarar una clase que herede a la clase __forms.Form__ donde declaremos los campos de inputs que poseerá, definiendo sus tipos y atributos.

```python
class BloggerForm(forms.Form):
    nombre = form.CharField()
    apellido = form.CharField()
    ciudad = form.CharField()
    email = form.EmailField()
```

#### Tipos de inputs

Existe diferentes tipos de inputs. Por ejemplo:

    * BooleanField
    * CharField
    * ChoiceField
    * TypedChoiceField
    * DateField
    * DateTimeField
    * DecimalField
    * EmailField
    * FileField
    * FloatField
    * ImageField
    * IntegerField
    * GenericIPAddressField
    * MultipleChoiceField
    * TimeField
    * URLField.

Además, pueden poseer argumentos como:

    * required: Si es True no se puede dejar el input vacio, por default esta opción es True.
    * label: El texto para el label, si no se da se genera uno usando el nombre del atributo.
    * initial: Valor inicial que se mostrará.
    * validators: Lista de funciones para validar el dato de entrada.
    * error_messages: una lista de mensajes de rror para el input.

#### Validación

Existen varios lugares donde puedes validar los datos, una de ellas es redefinir el método
__clean_<nombre de atributo>__ para un atributo en especifico, veamos el siguente ejemplo:

```python
from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class BloggerForm(forms.Form):
    nombre = form.CharField()
    apellido = form.CharField()
    ciudad = form.CharField()
    email = form.EmailField()

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]

        # El nombre posee espacios
        if " " in nombre:
            raise ValidationError(_('Nombre incorrecto -  no debe tener espacios'))
        nombre = nombre.lower()
        return nombre
```

Se ha de notar dos puntos importantes en este ejemplo. Primero que el dato a validar se encuentra en el diccionario __self.cleaned_data["nombre del atributo"]__, y luego de modificarlo se retorna este mismo. Segundo, al ocurrir un error de validación debemos utilizar __raise ValidationError()__ para que sea manejado por Django.

Una vez creado el formulario, el siguiente paso en incluirlo en una vista.

Repetimos el procedimiento para agregar vistas. Comenzamos agregando el la nueva vista a las urls.

```python
    url(r"^$", views.index, name="index"),
    url(r"^posts$", views.posts, name="posts"),
    url(r"^post/(?P<post_id>[0-9]+)$", views.post),
    url(r"^bloggers$", views.bloggers, name="bloggers"),
    url(r"^me$", views.me, name="me"),

    url(r"^blogger/(?P<blogger_id>[0-9]+)$", views.blogger, name="blogger"),
    url(r"^blogger/add$", views.new_blogger, name="add-blogger"),
]
```

Luego agregamos la función de la vista, no olvidar importar las nuevas dependecias.


```python
from django.http import HttpResponse
from django.shortcuts import render, redirect

# authentication
from django.contrib.auth.decorators import login_required

# Importamos los modelos
from .models import Post, Blogger

# Importamos los formularios
from .forms import BloggerForm

# CODIGO DE LAS OTRAS VISTAS ...

@login_required
def new_blogger(request):
    if request.method == "POST":
        form = BloggerForm(request.POST)
        if form.is_valid():
            blogger_instance = Blogger()
            blogger_instance.nombre = form.cleaned_data["nombre"]
            blogger_instance.apellido = form.cleaned_data["apellido"]
            blogger_instance.ciudad = form.cleaned_data["ciudad"]
            blogger_instance.email = form.cleaned_data["email"]
            blogger_instance.save()
            return redirect("blogger", blogger_id=blogger_instance.pk)
    else:
        form = BloggerForm()
        return render(request,"new_blogger.html", {"form":form})

```

En este punto es necesario destacar que usaremos la misma función pero responderá diferente dependiendo del método a utilizar. Si el método es __POST__ procedemos a agregar datos a la BD y redireccionar. En el otro caso, deberemos mostrar el formulario.

Finalmente debemos agregar el template __new_blogger.html__

``` html
{% extends "base.html" %}
{% block content %}

    <form action="" method="post">
        {% csrf_token %}
        <table>
        {{ form }}
        </table>
        <input type="submit" value="Submit" />
    </form>

{% endblock %}
```

Además, para nuestra comodidad agregaremos un link hacia la url agregada en el index.

```html
{% extends "base.html" %}

{% block content %}
<h1>Blog Home</h1>

<p>Esta es la versión correspondiente la sesión 3</p>


<p><b>visitas:</b> {{ visitas }}</p>


{% if user.is_authenticated %}

{% endif %}
    <a href="{% url 'add-blogger'%}">Agregar un blogger</a>
{% endblock %}

```

## Clase ModelForm

Usar Form nos permite tener una completa flexibilidad en cuanto a la toma de datos del usuario se necesite, sin embargo al trabajar con modelos frecuentemente utilizamos el mismo tipo de formulario genérico. En este caso es recomendable utilizar __ModelForm__.

Modificaremos el formulario anterior para utilizar __ModelForm__.

```python
class BloggerForm(forms.ModelForm):
    def clean_nombre(self):
         nombre = self.cleaned_data["nombre"]

         # El nombre posee espacios
         if " " in nombre:
             raise ValidationError('Nombre incorrecto -  no debe tener espacios')
         nombre = nombre.lower()
         return nombre

    class Meta:
        model = Blogger
        fields = ["nombre", "apellido", "ciudad", "email"]
        labels = { "ciudad": "Ciudad actual" }
        help_texts = {"email" : "Ingresar un correo de contacto"}
```

Además, ModelForm puede generar la instancia del modelo en la vista, modificamos nuestra vista:

```python
@login_required
def new_blogger(request):
    if request.method == "POST":
        form = BloggerForm(request.POST)
        if form.is_valid():
            blogger_instance = form.save()
            return redirect("blogger", blogger_id=blogger_instance.pk)
    else:
        form = BloggerForm()
        return render(request,"new_blogger.html", {"form":form})
```

En la siguiente sección se discuten las vistas genericas.