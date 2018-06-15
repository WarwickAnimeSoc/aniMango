# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-12 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_info', '0002_auto_20161018_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyentry',
            name='academic_year',
            field=models.IntegerField(choices=[(1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017)], default=2017, max_length=4, verbose_name=b'Academic year starting'),
        ),
    ]
