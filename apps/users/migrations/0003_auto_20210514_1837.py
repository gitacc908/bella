# Generated by Django 2.2 on 2021-05-14 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('users', '0002_auto_20210514_1631'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmark',
            options={'verbose_name': 'Избранное', 'verbose_name_plural': 'Избранные'},
        ),
        migrations.AddField(
            model_name='bookmark',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product', verbose_name='Товар в избранном'),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bookmark', to=settings.AUTH_USER_MODEL, verbose_name='Избранное'),
            preserve_default=False,
        ),
    ]