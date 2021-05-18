from django.db import models
from django.db.models.fields import DecimalField
from autoslug import AutoSlugField
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from .choices import (
    COLOR_CHOICES, CYAN, CLOTHING_FABRIC_CHOICES, POLYESTER,
    SIZE_RANGE_CHOICES, XL, LENGTH_RANGE_CHOICES, FASHION_CHOICES,
    A_SILHOUETTE
)


class Category(MPTTModel):
    """
    Category model that has 3 fields and self-related
    """
    title = models.CharField(
        max_length=100, verbose_name='Наименование категории'
    )
    slug = models.SlugField(
        max_length=100, verbose_name='Ссылка на категорию', unique=True
    )
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children'
    )

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})


class Product(models.Model):

    """
        Contains data for product, m2m relation with Category
        and bunch of choice fields for product
        """
    categories = models.ManyToManyField(
        Category, verbose_name='Категория', related_name='products'
    )
    title = models.CharField(
        max_length=255, verbose_name='Наименование товара'
    )
    slug = AutoSlugField(
        populate_from='title', unique=True,
    )
    article = models.CharField(
        max_length=255, verbose_name='Артикул'
    )
    quantity = models.PositiveIntegerField(
        default=1, verbose_name='Количество продукта'
    )
    color = models.PositiveSmallIntegerField(
        verbose_name='Цвет продукта', choices=COLOR_CHOICES, default=CYAN
    )
    price = models.DecimalField(
        max_digits=9, decimal_places=2, verbose_name='Цена'
    )
    description = models.TextField(
        verbose_name='Описание товара'
    )
    fabric_structure = models.PositiveSmallIntegerField(
        verbose_name='Состав ткани', choices=CLOTHING_FABRIC_CHOICES,
        default=POLYESTER
    )
    size_range = models.PositiveSmallIntegerField(
        verbose_name='Размерный ряд', choices=SIZE_RANGE_CHOICES,
        default=XL
    )
    length = models.PositiveSmallIntegerField(
        verbose_name='Длина', choices=LENGTH_RANGE_CHOICES,
        default=XL
    )
    fashion = models.PositiveSmallIntegerField(
        verbose_name='Фасон', choices=FASHION_CHOICES,
        default=A_SILHOUETTE
    )
    discount = models.PositiveSmallIntegerField(
        verbose_name='Скидка в процентах', blank=True, null=True
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг', default=0
    )
    created = models.DateTimeField(
        verbose_name='Дата создания', auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = "Products"
        ordering = ('-created',)

    def __str__(self):
        return f'Заголовок: {self.title}'

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})
