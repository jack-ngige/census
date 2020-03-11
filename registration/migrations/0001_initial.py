# Generated by Django 2.1 on 2019-09-08 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BirthRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('middle_name', models.CharField(max_length=250)),
                ('surname', models.CharField(max_length=250)),
                ('gender', models.CharField(choices=[('male', 'M'), ('female', 'F')], default='male', max_length=10)),
                ('date_of_birth', models.DateField()),
                ('mothers_name', models.CharField(max_length=250)),
                ('fathers_name', models.CharField(max_length=250)),
                ('county', models.CharField(choices=[('nairobi', 'Nairobi'), ('kisumu', 'Kisumu'), ('nakuru', 'Nakuru'), ('mombasa', 'Mombasa'), ('nyeri', 'Nyeri'), ('uasin gishu', 'Uasin Gishu'), ('baringo', 'Baringo'), ('narok', 'Narok')], default='nairobi', max_length=50)),
                ('constituency', models.CharField(max_length=300)),
                ('reference_number', models.CharField(blank=True, max_length=50)),
                ('id_no', models.PositiveIntegerField()),
                ('birth_cert_no', models.CharField(max_length=250)),
                ('birth_reg_date', models.DateTimeField(auto_now_add=True)),
                ('birth_reg_updated', models.DateTimeField(auto_now=True)),
                ('birth_author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DeathRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_death', models.DateField()),
                ('current_county', models.CharField(choices=[('nairobi', 'Nairobi'), ('kisumu', 'Kisumu'), ('nakuru', 'Nakuru'), ('mombasa', 'Mombasa'), ('nyeri', 'Nyeri'), ('uasin gishu', 'Uasin Gishu'), ('baringo', 'Baringo'), ('narok', 'Narok')], default='nairobi', max_length=50)),
                ('current_constituency', models.CharField(max_length=300)),
                ('status', models.CharField(choices=[('single', 'SINGLE'), ('married', 'MARRIED'), ('child', 'CHILD')], default='single', max_length=50)),
                ('children', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='no', max_length=50)),
                ('children_no', models.PositiveIntegerField(blank=True)),
                ('death_cert_no', models.CharField(max_length=250)),
                ('death_reg_date', models.DateTimeField(auto_now_add=True)),
                ('death_reg_updated', models.DateTimeField(auto_now=True)),
                ('death_author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationCentre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_centre_name', models.CharField(max_length=250)),
                ('reg_centre_type', models.CharField(choices=[('police post', 'POLICE POST'), ('hospital', 'HOSPITAL'), ('health centre', 'HEALTH CENTRE'), ('dispensary', 'DISPENSARY'), ('registrar office', 'REGISTRAR OFFICE')], default='hospital', max_length=50)),
                ('reg_centre_county', models.CharField(choices=[('nairobi', 'Nairobi'), ('kisumu', 'Kisumu'), ('nakuru', 'Nakuru'), ('mombasa', 'Mombasa'), ('nyeri', 'Nyeri'), ('uasin gishu', 'Uasin Gishu'), ('baringo', 'Baringo'), ('narok', 'Narok')], default='nairobi', max_length=50)),
                ('reg_centre_email', models.EmailField(max_length=50)),
                ('reg_centre_location', models.CharField(max_length=250)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('reg_updated', models.DateTimeField(auto_now=True)),
                ('reg_author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='admins', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='deathregistration',
            name='death_reg_centre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='death_registration_centres', to='registration.RegistrationCentre'),
        ),
        migrations.AddField(
            model_name='deathregistration',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person', to='registration.BirthRegistration'),
        ),
        migrations.AddField(
            model_name='birthregistration',
            name='birth_reg_centre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='birth_registration_centres', to='registration.RegistrationCentre'),
        ),
    ]
