from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
from django.views.generic.detail import DetailView

# Create your views here.


class ProductListView(ListView):
    model = Product
    context_object_name = 'product'
    template_name = 'store_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'store_detail.html'






