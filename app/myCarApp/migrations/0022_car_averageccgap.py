# Generated by Django 2.1 on 2020-09-18 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCarApp', '0021_lesseeprofile_cars_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='averageCcGap',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
