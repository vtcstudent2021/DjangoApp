from django.urls import path

from . import views

app_name = "store"

urlpatterns = [
    path("", views.product_all, name="product_all"),
    path("<slug:slug>", views.product_detail, name="product_detail"),
    path("product/<slug:category_slug>/", views.category_list, name="category_list"),
    path("about/", views.about, name="about"),
]
