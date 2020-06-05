from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView 
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


@login_required
def index_view(request, pk=None):
    if pk is None and request.user.is_authenticated:
        pk = request.user.pk
    user = get_object_or_404(User, pk=pk)
    return render(request, "user/index.html", {"user":user})

class login_view(LoginView):
    template_name = "user/login.html"

def register_view(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    return render(request, "user/register.html", {"form":form})

@login_required
def logout_view(request):
    logout(request)
    return redirect("login")
    
             