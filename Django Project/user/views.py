from django.views.generic import CreateView
from .models import CustomUser
from .forms import CustomUserCreationForm

class UserRegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = '/'