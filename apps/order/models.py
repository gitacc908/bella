from django.db import models
from django.contrib.auth import get_user_model

from apps.order.choices import PAYMENT_CHOICES
from apps.product.models import Product

User = get_user_model()


class Order(models.Model):
    """
    Order model that has all required information about user's order
    """
    owner = models.ForeignKey(
        User, verbose_name='Владелец заказа', blank=True, null=True, related_name='orders',
        on_delete=models.CASCADE)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания заказа')
    is_paid = models.BooleanField(
        default=False, verbose_name='Оплачено')
    buying_type = models.PositiveSmallIntegerField(
        choices=PAYMENT_CHOICES, verbose_name='Тип оплаты')
    is_delivered = models.BooleanField(
        default=False, verbose_name='Доставлено')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        if self.owner:
            return f'Заказ пользователя: {self.owner.phone}'
        else:
            return f'Заказ от анонимного пользователя'


class OrderItem(models.Model):
    """
    OrderItem model that store data about all user's buying products, product price and product quantity
    """
    owner = models.ForeignKey(
        User, verbose_name='Владелец купленного товара', blank=True, null=True,
        related_name='order_items', on_delete=models.CASCADE)
    order = models.ForeignKey(
        Order, verbose_name='Заказ', related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, verbose_name='Товар', related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена товара за штуку')
    quantity = models.PositiveIntegerField(
        default=1, verbose_name='Количество товара')

    class Meta:
        verbose_name = 'Заказанный товар'
        verbose_name_plural = 'Заказанные товары'

    def get_cost(self):
        return self.price * self.quantity

    def __str__(self):
        if self.owner:
            return f'Заказ для {self.product.title} продукта \
                        от {self.order.owner.first_name} {self.order.owner.last_name}'
        else:
            return f'Заказ для {self.product.title} продукта от анонимного пользователя'
