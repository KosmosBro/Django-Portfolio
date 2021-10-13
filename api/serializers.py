from django.contrib.auth.models import User
from rest_framework import serializers

from shop.models import Company, Product, Cart, CartContent


class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'title']


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def update(self, instance, validated_data):
        companies = validated_data.pop("company", [])
        instance = super().update(instance, validated_data)
        for company in companies:
            instance.companies.add(company)
        instance.save()
        return instance


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartContentSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartContent
        fields = '__all__'
