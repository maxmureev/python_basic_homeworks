from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("products_list/", views.ProductsListView.as_view(), name="products_list"),
    path(
        "product/<int:pk>",
        views.ProductsDetailView.as_view(),
        name="product_detail",
    ),
    path("product/add/", views.ProductCreateView.as_view(), name="product_create"),
    path(
        "product/<int:pk>/edit/",
        views.ProductUpdateView.as_view(),
        name="product_edit",
    ),
    path(
        "product/<int:pk>/delete/",
        views.ProductDeleteView.as_view(),
        name="product_delete",
    ),
]
