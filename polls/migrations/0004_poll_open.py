# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-08-09 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20180809_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='open',
            field=models.BooleanField(default=True),
        ),
    ]
