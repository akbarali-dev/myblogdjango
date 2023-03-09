from django.shortcuts import render, redirect
from .models import Post, Comment


# Create your views here.
def test_function(request):
    posts = Post.objects.all()
    post = Post.objects.first()
    print("Test: ", post.image)
    return render(request, "blog/blog.html", {
        'posts': posts
    })


def home(request):
    posts = Post.objects.all()
    post = Post.objects.first()
    print("Test: ", post.image)
    return render(request, "blog/blog.html", {
        'posts': posts
    })


def post_by_id(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        comments = Comment.objects.filter(post_id=pk)

        ctx = {
            "post": post,
            "comments": comments,
        }

        return render(request, "blog/post-comment.html", ctx)
    except ModuleNotFoundError:
        return redirect("blog:home")
