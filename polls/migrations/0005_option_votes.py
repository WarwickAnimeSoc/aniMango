# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-08-11 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_poll_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='votes',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]