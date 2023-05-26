# Generated by Django 4.2.1 on 2023-05-17 09:25

from django.db import migrations, models
import django.db.models.functions.comparison


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': [models.OrderBy(django.db.models.functions.comparison.Cast('date_release', models.DateTimeField()), descending=True)]},
        ),
    ]
