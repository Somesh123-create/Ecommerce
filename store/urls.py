from django.urls import path
from .views import ProductListView, ProductDetailView, CategoryView


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('detail/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<slug:slug>/', CategoryView, name='product_category'),


]
