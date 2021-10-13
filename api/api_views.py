from django.contrib.auth.models import User
from rest_framework import viewsets

from .serializers import CompanySerializers, ProductSerializers, UserSerializers, CartSerializers, \
    CartContentSerializers
from shop.models import Company, Product, Cart, CartContent


class CompanyListAPIView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers


class ProductListAPIView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class UserListAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class CartListAPIView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers


class CartContentListAPIView(viewsets.ModelViewSet):
    queryset = CartContent.objects.all()
    serializer_class = CartContentSerializers
