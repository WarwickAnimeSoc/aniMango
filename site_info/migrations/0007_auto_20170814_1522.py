# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 15:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_info', '0006_auto_20170810_2121'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historyentry',
            options={'ordering': ['-academic_year'], 'verbose_name_plural': 'History Entries'},
        ),
    ]
