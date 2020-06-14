from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User


# Create your views here.
def index_view(request):
    return render(request, "main/index.html", {"posts":Post.objects.all()})

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = Post(topic=request.POST["topic"], content=request.POST["content"], creator=request.user)
            new_post.save()
            return redirect("index")
    else:
        form = PostForm()
    return render(request, "main/post.html", {"form":form})



