# Generated by Django 2.1 on 2019-11-05 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20191104_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='birthregistration',
            name='alive',
            field=models.BooleanField(default=True),
        ),
    ]