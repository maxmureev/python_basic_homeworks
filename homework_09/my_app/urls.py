from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("products_list/", views.products_list, name="products_list"),
    path("product/<int:product_id>", views.product_detail, name="product_detail"),
    path("product/<int:product_id>/edit/", views.product_edit, name="product_edit"),
    path("product/add/", views.product_create, name="product_create"),
    path("about/", views.about, name="about"),
]
