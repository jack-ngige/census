# Generated by Django 2.1 on 2019-09-13 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20190913_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='registration_centre',
        ),
    ]
