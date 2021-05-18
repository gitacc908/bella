from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    phone = models.CharField(
        unique=True, max_length=30, verbose_name='Номер телефона'
    )
    country = models.CharField(
        max_length=255, verbose_name='Страна доставки'
    )
    city = models.CharField(
        max_length=255, verbose_name='Город доставки'
    )
    favorite_products = models.ManyToManyField(
        Product, verbose_name='Товар в избранном'
    )

    username = None
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
