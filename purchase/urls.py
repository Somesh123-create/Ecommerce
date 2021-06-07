from django.urls import path
from .views import ProductCartView, ProductCheckOutView

urlpatterns = [
    path('product_cart/', ProductCartView.as_view(), name='product_cart'),
    path('product_checkout/', ProductCheckOutView.as_view(), name='product_checkout'),

]