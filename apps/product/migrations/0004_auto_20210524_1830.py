# Generated by Django 2.2 on 2021-05-24 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210521_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='Изображение'),
        ),
    ]
