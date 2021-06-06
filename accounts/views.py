from django.shortcuts import render
from django.views.generic import CreateView, RedirectView
from django.urls import reverse_lazy
from .forms import SignUpForm


# Create your views here.


class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


