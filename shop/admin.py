from django.contrib import admin

from shop.models import Product, Company, Cart, CartContent

admin.site.register(Company)
admin.site.register(Cart)
admin.site.register(CartContent)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
