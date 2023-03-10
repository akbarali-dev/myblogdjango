from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required


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
        print("nima chidvhvbkc")
        print(comments.first().user_fullname())
        ctx = {
            "post": post,
            "comments": comments,
        }

        return render(request, "blog/post-comment.html", ctx)
    except ModuleNotFoundError:
        return redirect("blog:home")


@login_required
def save_new_comment(request):
    if request.method == 'POST':
        post_id = request.POST['post_id']
        comment = request.POST['comment']
        user_id = request.user.pk
        Comment.objects.create(
            text=comment,
            post_id=post_id,
            user_id=user_id
        )
