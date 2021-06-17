from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, FormView
from .models import Product
from  category.models import Category

# Create your views here.


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all().filter(is_available=True)
    context_object_name = 'product'
    template_name = 'store_list.html'


    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        product_count = Product.objects.all().filter(is_available=True)
        counts = product_count.count()
        context['counts'] = counts
        return context


def CategoryView(request, slug):
    product_category = Product.objects.filter(category__slug=slug)
    product_count = product_category.count()
    return render(request, 'category.html', {'slug':slug, 'product_category':product_category, 'product_count':product_count})




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
        cart[str(self.kwargs['slug'])] = self.request.POST['amount']
        self.request.session['cart'] = cart
        return HttpResponseRedirect('/')
