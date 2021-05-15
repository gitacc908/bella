from django.db import models


class DeliveryInfo(models.Model):
    """
    DeliveryInfo model that stores information about deliver
    """
    body = models.TextField(
        verbose_name='Информация о доставке')
    created_at = models.DateTimeField(
        auto_now_add=True)

    class Meta:
        verbose_name = 'Информация о доставке'
        verbose_name_plural = 'Информации о доставке'

    def __str__(self):
        return 'Информация о доставке'
