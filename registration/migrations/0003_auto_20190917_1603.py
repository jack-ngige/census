# Generated by Django 2.1 on 2019-09-17 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20190917_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthregistration',
            name='id_no',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]