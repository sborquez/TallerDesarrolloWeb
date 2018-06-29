from django.http import HttpResponse
from django.shortcuts import render

# Datos para pruebas

usuarios = [
    {"id": 0, "nombre": "sebastian", "apellido": "borquez", "ciudad":"Valpariso"},
    {"id": 1, "nombre":"francisco", "apellido": "lara", "ciudad":"santiago"}
]

posts = [
    {"id": 0, "blogger":0, "titulo":"Primero Post", "contenido":"Este es el primer post."},
    {"id": 1, "blogger":0,"titulo": "Segundo Post", "contenido": "Este es el contenido del segundo post"},
    {"id": 2, "blogger":1, "titulo": "Tercer Post", "contenido": "Y Este es el tercer post del blog"}
]


# Create your views here.
def index(request):
    #return HttpResponse('Hello World!')
    return HttpResponse('<h1>Hello World!</h1><p>El servidor está corriendo</p>')

"""
def blog(request, blog_id):
    try:
        blog_id = int(blog_id)
        return HttpResponse('<h1>{0}</h1><p>{1}</p>'.format(posts[blog_id]["titulo"], posts[blog_id]["contenido"]))
    except:
        return HttpResponse('<h1>No existe el </h1>')
"""

def blog(request, blog_id):
    try:
        blog_id = int(blog_id)
        return render(
            request,
            'post.html',
            context={'titulo':posts[blog_id]["titulo"], "contenido":posts[blog_id]["contenido"]},
        )
    except:
        return HttpResponse('<h1>No existe el blog</h1>')

def blogs(request):
    #return HttpResponse('<h1>No existe el blog</h1>')
    return render(request, "posts.html", context={"posts":posts})


