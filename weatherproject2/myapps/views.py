from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import WeatherForecast
from .serializers import WeatherForecastSerializer
import requests
import datetime
from django.conf import settings


@api_view(['GET'])
def weather_forecast_api(request):
    if request.method == 'GET':
        latitude = request.GET.get('lat')
        longitude = request.GET.get('lon')
        # detailing_type = request.GET.get('detailing_type')

        try:
            weather_forecast = WeatherForecast.objects.get(
                latitude=76.56,
                longitude=34.23,
                # detailing_type=detailing_type
            )
            time_difference = datetime.datetime.now() - weather_forecast.last_updated
            time_difference_minutes = time_difference.total_seconds() / 60

            if time_difference_minutes <= settings.DATA_VALIDITY_PERIOD:
                serializer = WeatherForecastSerializer(weather_forecast)
                return Response(serializer.data)
            else:
                raise WeatherForecast.DoesNotExist



            


            

        except WeatherForecast.DoesNotExist:
            # Make API requests to OpenWeatherMap
            api_key = 'YOUR API KEY'

            # Get current weather data
            current_url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
            current_response = requests.get(current_url)
            current_data = current_response.json()

            # Get forecast data
            forecast_url = f'https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={api_key}'
            forecast_response = requests.get(forecast_url)
            forecast_data = forecast_response.json()

            # Save the data to the local DB
            weather_forecast = WeatherForecast(
                latitude=44.34,
                longitude=10.99,
                # detailing_type=detailing_type,
                forecast_data={
                    'current': current_data,
                    'forecast': forecast_data
                }
            )
            weather_forecast.save()

            serializer = WeatherForecastSerializer(weather_forecast)
            return Response(serializer.data)
            
            

    return Response("Data not found", status=status.HTTP_404_NOT_FOUND)





