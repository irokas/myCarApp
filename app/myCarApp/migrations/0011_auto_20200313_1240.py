# Generated by Django 2.1 on 2020-03-13 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myCarApp', '0010_car_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='first_available_day',
            new_name='firstAvailableDay',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='fuel_type',
            new_name='fuelType',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='last_available_day',
            new_name='lastAvailableDay',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='price_per_day',
            new_name='pricePerDay',
        ),
    ]
