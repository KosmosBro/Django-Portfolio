# Generated by Django 3.2.7 on 2021-09-30 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20210928_2149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
