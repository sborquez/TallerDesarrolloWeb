from . import views
from django.urls import path
from django.urls import include
from django.conf.urls import url

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^posts$", views.posts, name="posts"),
    url(r"^blogger/add$", views.new_blogger, name="add-blogger"),
    url(r"^post/(?P<post_id>[0-9]+)$", views.post),
    url(r"^bloggers$", views.bloggers, name="bloggers"),
    url(r"^blogger/(?P<blogger_id>[0-9]+)$", views.blogger, name="blogger"),
    url(r"^me$", views.me, name="me")
]

urlpatterns += [  
    url(r'^post/create/$', views.PostCreate.as_view(), name='post_create'),
    url(r'^post/(?P<pk>\d+)/update/$', views.PostUpdate.as_view(), name='post_update'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.PostDelete.as_view(), name='post_delete'),
]