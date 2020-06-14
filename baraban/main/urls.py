from django.urls import include, path
from .views import index_view, create_post

urlpatterns = [
    path("", index_view, name="index"),
    path("post", create_post, name="create_post")
]