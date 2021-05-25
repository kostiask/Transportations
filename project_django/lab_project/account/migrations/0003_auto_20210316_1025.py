# Generated by Django 3.1.7 on 2021-03-16 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210316_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='car',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_driver',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='nr_prawa_jazdy',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='ocena',
        ),
        migrations.AddField(
            model_name='profile',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Dzien narodzin'),
        ),
        migrations.AddField(
            model_name='profile',
            name='number_of_phon',
            field=models.CharField(blank=True, max_length=150, verbose_name='Numer telefonu'),
        ),
        migrations.AlterField(
            model_name='car',
            name='manufacture',
            field=models.CharField(max_length=150, verbose_name='Producent'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=150, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='car',
            name='nr_car',
            field=models.CharField(max_length=150, verbose_name='Numer samochodu'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%y/%m/%d/', verbose_name='Foto'),
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nr_prawa_jazdy', models.CharField(blank=True, max_length=200)),
                ('ocena', models.FloatField(blank=True, null=True)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.car')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='driver',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.driver'),
        ),
    ]
