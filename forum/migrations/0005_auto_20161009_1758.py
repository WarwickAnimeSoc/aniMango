# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-09 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_board_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='first',
        ),
        migrations.AddField(
            model_name='thread',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
