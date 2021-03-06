# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-06 08:07
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hr_system_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('mr.', 'Mr.'), ('ms.', 'Ms.'), ('mrs.', 'Mrs.')], max_length=20, null=True)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('dob', models.DateField(null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{6,15}$')])),
                ('home_phone_number', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{6,15}$')])),
                ('profile_img', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr_system_app.Company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
