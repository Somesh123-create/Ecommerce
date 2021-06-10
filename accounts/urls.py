from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserRegisterView
from .forms import LoginForm



urlpatterns = [
    path('sign_up/', UserRegisterView.as_view(), name='sign_up'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]



