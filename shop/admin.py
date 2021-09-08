from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from shop.models import Product, Company

admin.site.register(Company)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']
