# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-27 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_merge_20180827_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='voter_id',
            field=models.CharField(default='', editable=False, max_length=30),
        ),
    ]