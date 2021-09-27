from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from shop.models import Company


class LoginForm(forms.Form):
    """ Форма для входа в систему. """
    login = forms.CharField(label='Login', label_suffix='')
    password = forms.CharField(widget=forms.PasswordInput, required=False, label='Password', label_suffix='')


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput, required=False, label='Password', label_suffix='')
    password2 = forms.CharField(widget=forms.PasswordInput, required=False, label='Repeat Password', label_suffix='')

    class Meta:
        model = User
        fields = ('username', 'email')


class SearchForm(forms.Form):
    # required отвечает за то является ли поле обязательным
    search = forms.CharField(required=False,
                             label='', )
