from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User


# Create your views here.
def index_view(request):
    return render(request, "main/index.html", {"posts":Post.objects.all()})

@login_required
def create_post_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = Post(topic=request.POST["topic"], content=request.POST["content"], creator=request.user)
            new_post.save()
            return redirect("main:index")
    else:
        form = PostForm()
    return render(request, "main/add_post.html", {"form":form})


@login_required
def comments_view(request, pk):
    post = Post.objects.get(pk=pk)
    comments = post.comments.all()
    if request.method == "POST":
            new_comment = Comment(post=post, content=request.POST["content"], creator=request.user)
            new_comment.save()
            return redirect("main:comments", pk)
    else:
        form = CommentForm()
    return render(request, "main/comments.html", {"form":form, "post":post, "comments":comments})



