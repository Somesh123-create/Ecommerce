from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class ProductCartView(TemplateView):
    template_name = 'order_cart.html'


class ProductCheckOutView(TemplateView):
    template_name = 'order_checkout.html'

