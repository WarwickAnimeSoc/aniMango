# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-10-12 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_info', '0011_homealert_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homealert',
            options={'verbose_name_plural': 'Alerts'},
        ),
        migrations.AlterField(
            model_name='homealert',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
