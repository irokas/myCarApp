# Generated by Django 2.1 on 2020-03-12 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myCarApp', '0006_auto_20200312_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.RenameField(
            model_name='lesseeprofile',
            old_name='User',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='lessorprofile',
            old_name='User',
            new_name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
