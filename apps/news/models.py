from django.db import models


class New(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование новости')
    slug = models.SlugField(max_length=100, verbose_name='Ссылка на новость', unique=True)
    body = models.TextField(verbose_name='Текст новости')
    draft = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news/', verbose_name='Фотография новости', blank=True, null=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
