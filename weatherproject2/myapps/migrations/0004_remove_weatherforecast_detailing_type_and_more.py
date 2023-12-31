# Generated by Django 4.1.5 on 2023-07-11 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0003_alter_weatherforecast_detailing_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weatherforecast',
            name='detailing_type',
        ),
        migrations.RemoveField(
            model_name='weatherforecast',
            name='forecast_data',
        ),
        migrations.RemoveField(
            model_name='weatherforecast',
            name='last_updated',
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='base',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='city_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='city_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='clouds',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='dt',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='feels_like',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='grnd_level',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='humidity',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='pressure',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='rain_1h',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='rain_3h',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='sea_level',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='snow_1h',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='snow_3h',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='sunrise',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='sunset',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='temp_max',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='temp_min',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='temperature',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='timezone',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='visibility',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='weather_description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='weather_icon',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='weather_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='weather_main',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='wind_deg',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='wind_gust',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='weatherforecast',
            name='wind_speed',
            field=models.FloatField(null=True),
        ),
    ]
