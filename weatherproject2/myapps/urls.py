from django.urls import path
from myapps.views import weather_forecast_api

urlpatterns = [
    path('api/weather-forecast/', weather_forecast_api),
]
