from django import forms
####USER PAGE VVVVV
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = get_user_model()
        fields = ['email', 'password1', 'password2']
