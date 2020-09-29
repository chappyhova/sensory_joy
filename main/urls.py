from django.contrib import admin
from django.urls import path
from . import views
from .views import ProductDetailView, ProductListView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('basket/', views.basket, name='basket'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<slug:slug>', ProductDetailView.as_view(), name='product_detail'),
    path('products/', views.products, name='products'),
    path('<slug:slug>/', views.update_basket, name='update_basket'),
]