from django.db import models





class WeatherForecast(models.Model):
    # latitude = models.FloatField(null=True)
    # longitude = models.FloatField(null=True)
    # # weather_id = models.IntegerField(null=True)
    # # weather_main = models.CharField(max_length=200,null=True)
    # # weather_description = models.CharField(max_length=200,null=True)
    # # weather_icon = models.CharField(max_length=200,null=True)
    # base = models.CharField(max_length=200,null=True)
    # # temperature = models.FloatField(null=True)
    # # feels_like = models.FloatField(null=True)
    # # pressure = models.FloatField(null=True)
    # # humidity = models.FloatField(null=True)
    # # temp_min = models.FloatField(null=True)
    # # temp_max = models.FloatField(null=True)
    # # sea_level = models.FloatField(null=True)
    # # grnd_level = models.FloatField(null=True)
    # visibility = models.FloatField(null=True)
    # # wind_speed = models.FloatField(null=True)
    # # wind_deg = models.FloatField(null=True)
    # # wind_gust = models.FloatField(null=True)
    # # clouds = models.FloatField(null=True)
    # # rain_1h = models.FloatField(null=True)
    # # rain_3h = models.FloatField(null=True)
    # # snow_1h = models.FloatField(null=True)
    # # snow_3h = models.FloatField(null=True)
    # # dt = models.DateTimeField(null=True)
    # # country = models.CharField(max_length=200,null=True)
    # # sunrise = models.DateTimeField(null=True)
    # # sunset = models.DateTimeField(null=True)
    # timezone = models.IntegerField(null=True)
    # # id = models.IntegerField(default=1)
    # name = models.CharField(max_length=200,null=True)
    # cod = models.TextField(null=True)

    # def __str__(self):
    #     return f"City: {self.name}, Base: {self.base}"
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    # detailing_type = models.CharField(max_length=20)
    forecast_data = models.JSONField(null=True)

    def __str__(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}"
    



    


