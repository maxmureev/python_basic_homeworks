from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.forms.models import model_to_dict

from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Product
from .forms import ProductModelForm


# Create your views here.
def index(request):
    return render(request, "my_app/index.html")


class ProductsListView(ListView):
    """ProductsListView"""

    model = Product
    template_name = "my_app/products_list.html"
    context_object_name = "products"


class ProductsDetailView(DetailView):
    """Product detail"""

    model = Product
    template_name = "my_app/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_fields"] = model_to_dict(self.object)
        return context


class ProductCreateView(CreateView):
    """Create new product"""

    model = Product
    template_name = "my_app/product_create.html"
    form_class = ProductModelForm
    success_url = reverse_lazy("products_list")


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "my_app/product_edit.html"
    form_class = ProductModelForm
    success_url = reverse_lazy("products_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "my_app/product_delete.html"
    success_url = reverse_lazy("products_list")


def about(request):
    return HttpResponse("About author")
