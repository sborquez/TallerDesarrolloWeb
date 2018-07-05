from django.http import HttpResponse
from django.shortcuts import render

# Importamos los modelos
from .models import Post, Blogger

# Datos para pruebas

_bloggers = [
    {"id": 0, "nombre": "sebastian", "apellido": "borquez", "ciudad":"Valpariso"},
    {"id": 1, "nombre":"francisco", "apellido": "cortinez", "ciudad":"Santiago"}
]

_posts = [
    {"id": 0, "blogger":0, "titulo":"Primero Post", "contenido":"Este es el primer post."},
    {"id": 1, "blogger":0,"titulo": "Segundo Post", "contenido": "Este es el contenido del segundo post"},
    {"id": 2, "blogger":1, "titulo": "Tercer Post", "contenido": "Y Este es el tercer post del post"}
]


# Create your views here.
def index(request):
    return render(request, "index.html")

def posts(request):
    posts_plus = Post.objects.all()
    return render(request, "posts.html", context={"posts":posts_plus})

def post(request, post_id):
    try:
        post_id = int(post_id)
        _post = Post.objects.get(id__exact=post_id)
        return render(
            request,
            'post.html',
            context={\
                "titulo":_post.titulo,
                "contenido":_post.contenido,
                "blogger": _post.blogger
            },
        )
    except:
        return HttpResponse('<h1>No existe el post</h1>')


def bloggers(request):
    _bloggers = Blogger.objects.all()
    return render(request, "bloggers.html", context={"bloggers":_bloggers})


def blogger(request, blogger_id):
    try:
        blogger_id = int(blogger_id)
        _blogger = Blogger.objects.get(id__exact=blogger_id)
        _posts = Post.objects.filter(blogger__id = blogger_id)
        return render(
            request,
            'blogger.html',
            context={ \
                "nombre":_blogger.nombre,
                "apellido":_blogger.apellido,
                "ciudad":_blogger.ciudad,
                "posts": _posts}
        )
    except Exception as err:
        print(err)
        return HttpResponse('<h1>No existe el post</h1>')

