# Generated by Django 2.1.3 on 2018-11-09 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('withdrawal_point', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='withdrawalpoint',
            options={'verbose_name': 'Withdrawal point', 'verbose_name_plural': 'Withdrawal points'},
        ),
        migrations.AlterField(
            model_name='withdrawalpoint',
            name='bank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bank.Bank'),
        ),
        migrations.AlterField(
            model_name='withdrawalpoint',
            name='is_disabled_access',
            field=models.NullBooleanField(default=None, verbose_name='is disabled access?'),
        ),
        migrations.AlterField(
            model_name='withdrawalpoint',
            name='is_nfc',
            field=models.NullBooleanField(default=None, verbose_name='is NFC?'),
        ),
    ]