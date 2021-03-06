from django.http import HttpResponse
from django.shortcuts import render

# authentication
from django.contrib.auth.decorators import login_required

# Importamos los modelos
from .models import Post, Blogger

# Create your views here.
def index(request):
    visitas = request.session.get("visitas", 0)
    request.session["visitas"] = visitas + 1
    return render(request, "index.html", context={"visitas": visitas})

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

@login_required
def me(request):
    return render(request, "me.html")