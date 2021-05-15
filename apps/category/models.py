from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


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
        'self', on_delete=models.CASCADE, null=True,
        blank=True, related_name='children'
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
