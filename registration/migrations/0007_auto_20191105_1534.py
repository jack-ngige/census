# Generated by Django 2.1 on 2019-11-05 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_birthregistration_alive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deathregistration',
            name='children_no',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
