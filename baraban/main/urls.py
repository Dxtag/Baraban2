from django.urls import include, path
from .views import index_view, create_post_view, comments_view, delete_post_view

app_name = "main"

urlpatterns = [
    path("", index_view, name="index"),
    path("create", create_post_view, name="create_post"),
    path("post/<int:pk>", comments_view, name="comments"),
    path("post/<int:pk>/delete", delete_post_view, name="delete_post")
]