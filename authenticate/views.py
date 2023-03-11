from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserForm


# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog:home')
        else:
            messages.success(request, "password or login error")
            return redirect('login-user')
    else:
        return render(request, "authenticate/login.html")


def logout_user(request):
    logout(request)
    messages.success(request, "You we logged out")
    return redirect('blog:home')


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm()
        if request.user.is_authenticated:
            messages.success(request, ("You have already registered!",))
            return redirect('register-user')
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # if username and password:
            #     User.objects.create(
            #         password=password,
            #         username=username
            #     )
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration successfully",))
            return redirect('blog:home')
        else:
            print(request.POST['password1'])
            print(request.POST['password2'])
            messages.success(request, ("password or username is incomplete",))
            return render(request, "authenticate/register.html")

    else:
        form = UserCreationForm()
        return render(request, "authenticate/register.html", {
            "form": form
        })
