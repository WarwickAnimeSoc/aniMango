# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-24 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0014_auto_20170810_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='cooldown_date',
            field=models.DateField(null=True),
        ),
    ]