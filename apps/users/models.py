from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models
from django.db.models.signals import post_save

from apps.product.models import Product


class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, phone, password=None, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not phone:
            raise ValueError('The given phone must be set')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password=None, **extra_fields):
        """Create and save a SuperUser with the given phone and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields)


class CustomUser(AbstractUser):
    """Customising default django user to our fields"""
    phone = models.CharField(unique=True, max_length=30, verbose_name='Номер телефона')
    country = models.CharField(max_length=200, verbose_name='Страна доставки')
    city = models.CharField(max_length=150, verbose_name='Город доставки')
    username = None
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Bookmark(models.Model):
    """
    Bookmark model that contains user wishes product
    related with User and Product models
    """
    user = models.OneToOneField(CustomUser, verbose_name='Избранное', on_delete=models.CASCADE,
                                related_name='bookmark')
    product = models.ForeignKey(Product, verbose_name='Товар в избранном', on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

    def __str__(self):
        return f'{self.user.first_name} добавил в избранное {self.product.title}'


def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        Bookmark.objects.create(user=instance)


post_save.connect(post_save_receiver, sender=CustomUser)
