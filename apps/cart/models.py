from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Cart(models.Model):
    """
    Cart model for customer purchases
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = "Carts"
        ordering = ('-id',)

    def __str__(self):
        return f'Cart with Owner: {self.owner},'
