# Generated by Django 2.2.13 on 2020-10-25 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0002_viewcounter_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='view',
            name='token',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]