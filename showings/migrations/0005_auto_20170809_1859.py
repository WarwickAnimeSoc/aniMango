# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 18:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showings', '0004_auto_20161021_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='ani_link',
        ),
        migrations.RemoveField(
            model_name='show',
            name='anilist_anime_number',
        ),
        migrations.RemoveField(
            model_name='show',
            name='mal_link',
        ),
        migrations.RemoveField(
            model_name='show',
            name='title',
        ),
        migrations.RemoveField(
            model_name='show',
            name='title_eng',
        ),
        migrations.RemoveField(
            model_name='show',
            name='wiki_link',
        ),
        migrations.AlterField(
            model_name='show',
            name='lib_series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='library.Series'),
            preserve_default=False,
        ),
    ]
