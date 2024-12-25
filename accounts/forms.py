from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = [ 'first_name', 'last_name', 'email','password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email', required=True)
