# Generated by Django 2.2.5 on 2019-11-27 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_profile_registration_centre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='registration_centre',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='employees_reg_centres', to='registration.RegistrationCentre'),
        ),
    ]
