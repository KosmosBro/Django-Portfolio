# Generated by Django 3.1.6 on 2021-09-11 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210908_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='img',
            field=models.ImageField(blank=True, max_length=900, upload_to='images/', verbose_name='Картинка компании'),
        ),
    ]