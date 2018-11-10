# Generated by Django 2.1.3 on 2018-11-09 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name': 'валюта', 'verbose_name_plural': 'валюты'},
        ),
        migrations.AlterField(
            model_name='currency',
            name='iso_name',
            field=models.CharField(max_length=3, unique=True, verbose_name='ISO 4217'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='название'),
        ),
    ]
