from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.forms.models import model_to_dict
from .models import Product
from .forms import ProductModelForm


# Create your views here.
def index(request):
    return render(request, "my_app/index.html")


def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "my_app/products_list.html", context=context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        "product": product,
        "product_fields": model_to_dict(product),  # Добавлено
    }
    return render(request, "my_app/product_detail.html", context=context)


def product_create(request):
    """form = PostModelForm()"""
    if request.method == "POST":
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products_list")
    else:
        form = ProductModelForm()
    context = {"form": form, "title": "Добавление поста"}
    return render(request, "my_app/product_create.html", context=context)


def product_edit(request, product_id):
    """form = PostModelForm()"""

    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        form = ProductModelForm(request.POST, instance=product)
        if form.is_valid():

            form.save()
            return redirect("products_list")
    else:
        form = ProductModelForm(instance=product)
    context = {"form": form, "title": "Изменение поста"}
    return render(request, "my_app/product_edit.html", context=context)


def about(request):
    return HttpResponse("About author")
