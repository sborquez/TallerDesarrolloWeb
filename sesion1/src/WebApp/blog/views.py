from django.http import HttpResponse
from django.shortcuts import render

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
    return HttpResponse('<h1>Bienvenido a tu Blog</h1><p>Esta es la versión correspondiente al ejercicio de práctica de la sesión 1</p>')

def posts(request):
    #return HttpResponse('<h1>No existe el post</h1>')
    posts_plus = []
    for post in _posts:
        post_plus = dict(post)
        post_plus["blogger"] = _bloggers[post["blogger"]]
        posts_plus.append(post_plus)
    return render(request, "posts.html", context={"posts":posts_plus})

"""
def post(request, post_id):
    try:
        post_id = int(post_id)
        return HttpResponse('<h1>{0}</h1><p>{1}</p>'.format(posts[post_id]["titulo"], posts[post_id]["contenido"]))
    except:
        return HttpResponse('<h1>No existe el </h1>')
"""

def post(request, post_id):
    try:
        post_id = int(post_id)
        blogger = _bloggers[_posts[post_id]["blogger"]]
        print(blogger)
        return render(
            request,
            'post.html',
            context={\
                "titulo":_posts[post_id]["titulo"],
                "contenido":_posts[post_id]["contenido"],
                "blogger": blogger
            },
        )
    except:
        return HttpResponse('<h1>No existe el post</h1>')


def bloggers(request):
    return render(request, "bloggers.html", context={"bloggers":_bloggers})


def blogger(request, blogger_id):
    try:
        blogger_id = int(blogger_id)
        posts = []
        for post in _posts:
            print(post)
            if blogger_id == post["blogger"]:
                posts.append(post)
        return render(
            request,
            'blogger.html',
            context={ \
                "nombre":_bloggers[blogger_id]["nombre"],
                "apellido":_bloggers[blogger_id]["apellido"],
                "ciudad":_bloggers[blogger_id]["ciudad"],
                "posts": posts}
        )
    except Exception as err:
        print(err)
        return HttpResponse('<h1>No existe el post</h1>')

