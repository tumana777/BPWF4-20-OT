from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

class UserRegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('user:login')

class UserLoginView(LoginView):
    template_name = 'login.html'
    next_page = '/'