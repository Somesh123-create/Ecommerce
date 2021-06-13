from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from .models import Product

# Create your views here.


class ProductListView(ListView):
    model = Product
    context_object_name = 'product'
    template_name = 'store_list.html'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     try:
    #         carr_list = self.request.session['cart']
    #         context['cart'] = carr_list
    #     except:
    #         pass
    #     return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'store_detail.html'

    def post(self, request, *args, **kwargs):
        cart = self.request.session.get("cart", {})
        cart[str(self.kwargs['pk'])] = self.request.POST['amount']
        self.request.session['cart'] = cart
        return HttpResponseRedirect('/')












