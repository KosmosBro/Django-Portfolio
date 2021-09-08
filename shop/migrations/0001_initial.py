# Generated by Django 3.1.6 on 2021-09-08 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название продукта')),
                ('descriptions', models.CharField(max_length=250, verbose_name='описание продукта')),
                ('price', models.PositiveIntegerField(verbose_name='цена продукта')),
                ('img', models.ImageField(blank=True, max_length=900, upload_to='images/', verbose_name='Картинка продукта')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
