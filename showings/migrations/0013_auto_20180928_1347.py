# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-28 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showings', '0012_auto_20180220_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showing',
            name='showing_type',
            field=models.CharField(choices=[('wk', 'Weekly showing'), ('an', 'Allnighter'), ('ev', 'Event'), ('mo', 'Movie Night'), ('ot', 'Other')], default='wk', max_length=2),
        ),
    ]
