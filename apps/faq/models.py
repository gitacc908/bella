from django.db import models


class FAQ(models.Model):
    """
    FAQ models that stores all popular questions and answer to them
    """
    question = models.CharField(max_length=100, verbose_name='Вопрос')
    answer = models.CharField(max_length=100, verbose_name='Ответ')

    def __str__(self):
        return 'FAQ'
