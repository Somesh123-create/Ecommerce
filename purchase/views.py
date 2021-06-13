from django.shortcuts import render
from django.views.generic import TemplateView
from store.models import Product

# Create your views here.


class ProductCartView(TemplateView):
    template_name = 'order_cart.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            if len(self.request.session['cart']) >= 1:
                ids = list(self.request.session['cart'].keys())
                context['product'] = Product.get_product_by_id(ids)
        except:
            context['messages_cart'] = "Sorry, Your cart is empty."
        # try:
        #     if len(self.request.session['cart']) >= 1:
        #         for x in self.request.session['cart']:
        #             j = Product.objects.get(id=self.request.session['cart'][x][0])
        #             my_list = j
        #             print(my_list)
        #             context['product'] = my_list
        # except:
        #     pass
        return context


class ProductCheckOutView(TemplateView):
    template_name = 'order_checkout.html'

