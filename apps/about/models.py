from django.db import models


class About(models.Model):
    """
    About model that store text about company and so on
    """
    body = models.TextField(verbose_name='Текст страницы "О нас"')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return 'О нас'
