# Generated by Django 4.1.5 on 2023-07-11 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0005_rename_city_name_weatherforecast_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherforecast',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]
