from django.urls import include, path
from .views import index_view, create_post_view, comments_view

app_name = "main"

urlpatterns = [
    path("", index_view, name="index"),
    path("post/create", create_post_view, name="create_post"),
    path("post/<int:pk>", comments_view, name="comments")
]