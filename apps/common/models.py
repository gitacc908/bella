from django.db import models


class About(models.Model):
    """
    About model that store text about company and so on
    """
    body = models.TextField(
        verbose_name='Текст страницы "О нас"'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата добавления'
    )

    def __str__(self):
        return 'О нас'


class Contact(models.Model):
    """
    Contact model that stores information about shop contacts, location
    """
    phone_number = models.CharField(
        max_length=50, verbose_name='Номер телефона магазина'
    )
    email = models.EmailField(
        max_length=50, verbose_name='Почтовый адрес магазина'
    )
    location = models.CharField(
        max_length=255, verbose_name='Адрес магазина'
    )

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return 'Контакты'


class DeliveryInfo(models.Model):
    """
    DeliveryInfo model that stores information about deliver
    """
    body = models.TextField(
        verbose_name='Информация о доставке'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Информация о доставке'
        verbose_name_plural = 'Информации о доставке'

    def __str__(self):
        return 'Информация о доставке'


class FAQ(models.Model):
    """
    FAQ models that stores all popular questions and answer to them
    """
    question = models.CharField(
        max_length=255, verbose_name='Вопрос'
    )
    answer = models.CharField(
        max_length=255, verbose_name='Ответ'
    )

    def __str__(self):
        return 'FAQ'


class News(models.Model):
    title = models.CharField(
        max_length=255, verbose_name='Наименование новости'
    )
    slug = models.SlugField(
        max_length=255, verbose_name='Ссылка на новость', unique=True
    )
    body = models.TextField(
        verbose_name='Текст новости'
    )
    draft = models.BooleanField(
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    image = models.ImageField(
        upload_to='news/', verbose_name='Фотография новости', blank=True, null=True
    )

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
