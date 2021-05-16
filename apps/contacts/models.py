from django.db import models


class Contact(models.Model):
    """
    Contact model that stores information about shop contacts, location
    """
    phone_number = models.CharField(
        max_length=100, verbose_name='Номер телефона магазина')
    email = models.EmailField(
        max_length=100, verbose_name='Почтовый адрес магазина')
    location = models.CharField(
        max_length=200, verbose_name='Адрес магазина')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return 'Контакты'
