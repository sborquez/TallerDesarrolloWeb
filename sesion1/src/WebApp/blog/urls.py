from . import views
from django.urls import path
from django.urls import include
from django.conf.urls import url

urlpatterns = [
    url(r"^$", views.index),
    url(r"^post/(?P<blog_id>[0-9])$", views.blog),
    url(r"^posts$", views.blogs),
]