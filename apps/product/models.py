from django.db import models

from apps.category.models import Category


class Product(models.Model):
    # Adilet's part
    category = models.ManyToManyField(Category, verbose_name='Категория', related_name='products')
    title = models.CharField(max_length=200, verbose_name='Наименование товара')
