# Generated by Django 4.2.11 on 2024-05-29 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Цена'),
        ),
    ]