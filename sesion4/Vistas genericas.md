# Vistas genericas

Al igual que al utilizar ModelForm para generar formularios genericos para los modelos, podemos crear vistas genericas para poder crear, modificar y eliminar instancias de nuestros modelos, sin la necesidad de que nosotros creemos los ModelForms ya que se la vista generica se encarga de esto.

Para esto necesitamos agregar el siguiente código, utilizaremos ahora el modelo Post

```python
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class PostCreate(CreateView):
    model = Post
    fields = '__all__'

class PostUpdate(UpdateView):
    model = Post
    fields = ['titulo','contenido']

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('posts')
```

Esto generará las tres vistas la cuales se encargarán de: crear un nuevo post, editar un post y eliminar un post. A continuación debemos agregar los templates, PostCreate y PostUpdate comparten el mismo template, este debe tener el nombre de __<nombre_modelo>_form.html__, los cuales estarán contendios dentro de una carpeta con el nombre del la aplicación, en nuestro caso debemos crear.

    WebApp\blog\templates\blog\post_form.html

```html
{% extends "base.html" %}

{% block content %}

<form action="" method="post">
    {% csrf_token %}
    <table>
    {{ form.as_table }}
    </table>
    <input type="submit" value="Submit" />
</form>
{% endblock %}
```

En cuanto al template para PostDelete, este debe llamarse __<nombre_modelo>_confirm_delete.html__. Creamos el archivo en la misma carpeta que el tempate anterior.

    WebApp\blog\templates\blog\post_confirm_delete.html

```html
{% extends "base.html" %}

{% block content %}

<h1>Borrar Post</h1>

<p>Está a punto de eliminar el post: {{ post }}?</p>

<form action="" method="POST">
  {% csrf_token %}
  <input type="submit" action="" value="Yes, delete." />
</form>

{% endblock %}
```

Finalmente como hemos hecho anteriormente, debemos agregar la url.

```python
urlpatterns += [  
    url(r'^post/create/$', views.PostCreate.as_view(), name='post_create'),
    url(r'^post/(?P<pk>\d+)/update/$', views.PostUpdate.as_view(), name='post_update'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.PostDelete.as_view(), name='post_delete'),
]
```

Además, para nuestra comodidad, agregaremos links a estas nuevas vistas.

En el template de index

```html
{% extends "base.html" %}

{% block content %}
<h1>Blog Home</h1>

<p>Esta es la versión correspondiente la sesión 4</p>


<p><b>visitas:</b> {{ visitas }}</p>


{% if user.is_authenticated %}

{% endif %}
    <a href="{% url 'add-blogger'%}">Agregar un blogger</a>
    <a href="{% url 'post_create'%}">Agregar un post</a>
{% endblock %}
```

Y en el template para posts

```html
{% extends "base.html" %}

{% block title %}<title>Posts</title>{% endblock %}
{% block content %}
    <h1>Posts</h1>
    <table>
        <tr>
            <th>id</th><th>titulo</th><th>blogger</th><th>Editar</th><th>Eliminar</th>
        </tr>
        {%for element in posts%}
            <tr>
                <td>{{element.id}}</td>
                <td><a href="/blog/post/{{ element.pk }}">{{element.titulo}}</a></td>
                <td><a href="/blog/blogger/{{element.blogger.id}}">{{element.blogger.nombre}} {{element.blogger.apellido}}</a>  </td>
                <td><a href="/blog/post/{{ element.pk }}/update/">x</a></td>
                <td><a href="/blog/post/{{ element.pk }}/delete/">x</a></td>
            </tr>
        {% endfor %}
    </table>
{% endblock %}
```