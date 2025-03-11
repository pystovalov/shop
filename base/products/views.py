from django.http.response import re
from django.shortcuts import render
from products.models import Product, ProductCategory


def index(request):
    context = {
        "title": "Index",
    }
    return render(request, "products/index.html", context)


def products(request):
    context = {
        "title": "Products",
        "category": ProductCategory.objects.all(),
        "products": Product.objects.all(),
    }
    return render(request, "products/products.html", context)
