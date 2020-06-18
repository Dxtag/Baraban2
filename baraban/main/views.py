from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
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
def delete_post_view(request, pk):
    post = get_object_or_404(Post,pk=pk)
    if post.creator == request.user:
        post.delete()
        return redirect("main:index")
    else:
        return HttpResponse("Error")

@login_required
def comments_view(request, pk):
    post = get_object_or_404(Post,pk=pk)
    comments = post.comments.all()
    if request.method == "POST":
            new_comment = Comment(post=post, content=request.POST["content"], creator=request.user)
            new_comment.save()
            return redirect("main:comments", pk)
    else:
        form = CommentForm()
    return render(request, "main/comments.html", {"form":form, "post":post, "comments":comments})

@login_required
def delete_comment_view(request, pk):
    comment = get_object_or_404(Comment,pk=pk)
    if comment.creator == request.user:
        comment.delete()
    return redirect("main:index") 



