# Generated by Django 2.1 on 2020-03-19 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCarApp', '0014_auto_20200319_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.FileField(upload_to='car_photos'),
        ),
    ]
