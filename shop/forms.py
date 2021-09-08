from django import forms


class LoginForm(forms.Form):
    """ Форма для входа в систему. """
    login = forms.CharField(label='Login', label_suffix='')
    password = forms.CharField(widget=forms.PasswordInput, required=False, label='Password', label_suffix='')
