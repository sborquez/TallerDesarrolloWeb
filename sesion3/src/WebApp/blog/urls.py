from . import views
from django.urls import path
from django.urls import include
from django.conf.urls import url

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^posts$", views.posts, name="posts"),
    url(r"^post/(?P<post_id>[0-9]+)$", views.post),
    url(r"^bloggers$", views.bloggers, name="bloggers"),
    url(r"^blogger/(?P<blogger_id>[0-9]+)$", views.blogger),
    url(r"^me$", views.me, name="me")
]