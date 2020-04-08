# Generated by Django 2.2.2 on 2019-06-16 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showings', '0014_merge_20190616_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showing',
            name='showing_type',
            field=models.CharField(choices=[('wk', 'Weekly showing'), ('an', 'Allnighter'), ('ev', 'Event'), ('mo', 'Movie Night'), ('ot', 'Other')], default='wk', max_length=2),
        ),
    ]