# Generated by Django 2.2.13 on 2020-06-23 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('karaoke', '0002_auto_20200422_0054'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='song',
            unique_together={('title', 'artist')},
        ),
    ]