from django.http.response import re
from django.shortcuts import render


def index(request):
    context = {
        "title": "Index",
    }
    return render(request, "products/index.html", context)


def products(request):
    return render(request, "products/products.html")
