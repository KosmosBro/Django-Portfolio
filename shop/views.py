from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from shop.forms import LoginForm


def view_home(request):

    """ view главной страницы. """

    user = request.user.get_username()
    return render(request, 'home.html', {'user': user})


def view_login(request):

    """ view входа в систему. """

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
            else:
                form.add_error('login', 'Bad login or password')
                form.add_error('password', 'Bad login or password')
                return render(request, 'log_in.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'log_in.html', {'form': form})
