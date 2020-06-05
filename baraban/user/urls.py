from django.urls import include, path
from .views import index_view, login_view, logout_view, register_view
from django.contrib.auth.models import User
from django.http import request


urlpatterns = [
    path("", index_view, name="index"),
    path("<int:pk>", index_view, name="index"),
    path("login", login_view.as_view(), name="login"),
    path("logout",logout_view , name="logout"),
    path("register", register_view, name="register")
]