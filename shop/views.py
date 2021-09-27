from django.contrib.auth import authenticate, login, logout
from django.contrib.postgres.search import SearchVector
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from shop.forms import LoginForm, RegisterForm, SearchForm
from shop.models import Product, Company, CartContent, Cart, UserProfile


def view_home(request):
    """ view главной страницы. """
    company = Company.objects.all()
    return render(request, 'home.html', {'company': company})


def view_product(request, slug):
    """ view страницы продуктов . """
    product = Product.objects.filter(company__slug=slug)
    return render(request, 'product.html', {'product': product})


def view_register(request):
    """ view регистрации пользователя. """
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.save()
            return redirect('/')
    else:
        user_form = RegisterForm()
    return render(request, 'register.html', {'user_form': user_form})


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


def view_log_out(request):
    """ view выход пользователя из системы. """
    logout(request)
    return redirect('/')


class MasterView(View):

    def get_cart_records(self, cart=None, response=None):
        cart = self.get_cart() if cart is None else cart
        if cart is not None:
            cart_records = CartContent.objects.filter(cart_id=cart.id)
        else:
            cart_records = []

        if response:
            response.set_cookie('cart_count', len(cart_records))
            return response

        return cart_records

    def get_cart(self):
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
            product_items = Product(id=self.request.COOKIES.get('product_id'))
            qty = 1
            try:
                cart = Cart.objects.get(user_id=user_id)
            except ObjectDoesNotExist:
                cart = Cart(user_id=user_id,
                            total_cost=0)
                cart.save()
                cart_content, _ = CartContent.objects.get_or_create(cart=cart, product=product_items)
                cart_content.qty = qty
                cart_content.save()

        else:
            session_key = self.request.session.session_key
            self.request.session.modified = True
            if not session_key:
                self.request.session.save()
                session_key = self.request.session.session_key
            try:
                cart = Cart.objects.get(session_key=session_key)
            except ObjectDoesNotExist:
                cart = Cart(session_key=session_key,
                            total_cost=0)
                cart.save()
        return cart


class CartView(MasterView):
    def get(self, request):
        cart = self.get_cart()
        cart_records = self.get_cart_records(cart)
        cart_total = cart.get_total() if cart else 0

        context = {
            'cart_records': cart_records,
            'cart_total': cart_total,
        }
        return render(request, 'cart.html', context)

    def post(self, request):
        product_items = Product.objects.get(id=request.POST.get('product_id'))
        cart = self.get_cart()
        quantity = request.POST.get('qty')
        cart_content, _ = CartContent.objects.get_or_create(cart=cart, product=product_items)
        cart_content.save()
        response = self.get_cart_records(cart, redirect('/#product-{}'.format(product_items.id)))
        product_id = product_items.id
        cart_content.qty = quantity
        response.set_cookie('qty', quantity)
        response.set_cookie('product_id', product_id)
        return response
