from django.urls import include, path
from .views import index_view, login_view, logout_view, register_view, password_change_view, password_reset_view
from django.contrib.auth.models import User
from django.http import request

app_name = "user"

urlpatterns = [
    path("", index_view, name="index"),
    path("<int:pk>", index_view, name="index"),
    path("login", login_view.as_view(), name="login"),
    path("logout",logout_view , name="logout"),
    path("register", register_view, name="register"),
    path("password_change", password_change_view.as_view(), name="password_change"),
    path("password_reset", password_reset_view.as_view(), name="password_reset")
]