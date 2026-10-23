from django.contrib.auth.forms import UserCreationForm
from user.models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    # test = forms.CharField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')