# Generated by Django 3.1.7 on 2021-04-20 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transportation_car', '0012_remove_transportation_car_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='transportation',
            name='car_owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='car_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
