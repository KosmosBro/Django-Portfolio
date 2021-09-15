from django.db import models


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
