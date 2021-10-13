from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name="Фото профиля", max_length=900)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('user', 'avatar')


class Company(models.Model):
    """ Сущность используется для добавления компании в модель _Product_ """
    img = models.ImageField(upload_to='images/', blank=True, verbose_name="Картинка компании", max_length=900)
    title = models.CharField(max_length=100, verbose_name='Компания')
    descriptions = models.CharField(max_length=250, verbose_name='описание компании')
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
        unique_together = ('title', 'slug')


class Product(models.Model):
    img = models.ImageField(upload_to='images/', blank=True, verbose_name="Картинка продукта", max_length=900)
    title = models.CharField(max_length=100, verbose_name='название продукта')
    company = models.ManyToManyField(Company, verbose_name='Компания')
    descriptions = models.CharField(max_length=250, verbose_name='описание продукта')
    price = models.PositiveIntegerField(verbose_name='цена продукта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        unique_together = ('title', 'price')


class Cart(models.Model):
    session_key = models.CharField(max_length=999, blank=True, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    total_cost = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user}{self.session_key}'

    def get_total(self):
        items = CartContent.objects.filter(cart=self.id)
        total = 0
        for item in items:
            total += item.product.price * item.qty
        return total

    def get_cart_content(self):
        items = CartContent.objects.all()
        return items

    class Meta:
        verbose_name = "Корзины"
        verbose_name_plural = "Корзина"


class CartContent(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(null=True, default=0)

    class Meta:
        verbose_name = "Контент корзины"
        verbose_name_plural = "Контент корзины"
        unique_together = ('cart', 'qty')

