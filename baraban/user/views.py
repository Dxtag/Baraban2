from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


@login_required
def index_view(request, pk=None):
    if pk is None and request.user.is_authenticated:
        pk = request.user.pk
    user = get_object_or_404(User, pk=pk)
    return render(request, "user/index.html", {"user":user})

def register_view(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
    return render(request, "user/form.html", {"form":form})

@login_required
def logout_view(request):
    logout(request)
    return redirect("user:login")

class login_view(LoginView):
    template_name = "user/login.html"

class password_change_view(PasswordChangeView):
    template_name = "user/form.html"
    success_url = "/"
    

class password_reset_view(PasswordResetView):
    template_name = "user/form.html"
    success_url = "/"
    
             