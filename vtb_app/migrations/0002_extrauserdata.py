# Generated by Django 3.1.2 on 2020-10-10 22:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vtb_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraUserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
                ('income_amount', models.IntegerField(blank=True, default=0)),
                ('birth_date_time', models.CharField(blank=True, default='', max_length=100)),
                ('birth_place', models.CharField(blank=True, default='', max_length=100)),
                ('family_name', models.CharField(blank=True, default='', max_length=100)),
                ('first_name', models.CharField(blank=True, default='', max_length=100)),
                ('gender', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female'), ('unknown', 'unknown')], default=('unknown', 'unknown'), max_length=100)),
                ('middle_name', models.CharField(blank=True, default='', max_length=100)),
                ('nationality_country_code', models.CharField(blank=True, default='', max_length=100)),
                ('phone', phone_field.models.PhoneField(blank=True, default='', max_length=31)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]