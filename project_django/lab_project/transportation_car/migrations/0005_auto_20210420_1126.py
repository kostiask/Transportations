# Generated by Django 3.1.7 on 2021-04-20 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation_car', '0004_auto_20210420_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportation',
            name='data_end_deliveri',
            field=models.DateTimeField(blank=True, default=None, verbose_name='Koniec terminu dostawy'),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='data_end_shipment',
            field=models.DateTimeField(blank=True, default=None, verbose_name='Koniec terminu nadania'),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='data_start_deliveri',
            field=models.DateTimeField(blank=True, default=None, verbose_name='Poczotek terminu dostawy'),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='data_start_shipment',
            field=models.DateTimeField(blank=True, default=None, verbose_name='Poczotek terminu nadania'),
        ),
    ]
