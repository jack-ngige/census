# Generated by Django 2.2.5 on 2019-11-12 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_auto_20191105_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='deathregistration',
            name='cause_of_death',
            field=models.CharField(default='Malaria', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deathregistration',
            name='occupation',
            field=models.CharField(default='Teacher', max_length=300),
            preserve_default=False,
        ),
    ]
