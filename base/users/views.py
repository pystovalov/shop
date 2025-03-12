from django.shortcuts import render
from users.models import User
from users.forms import UserLoginForm


def login(request):
    context = {
        "form": UserLoginForm(),
    }
    return render(request, "users/login.html", context)


def register(request):
    return render(request, "users/register.html")


def profile(request):
    return render(request, "users/profile.html")
