from django.urls import path
from .views import weather, weather_history
urlpatterns = [
    path('weather/<str:city_name>', weather),
    path('weather-history/', weather_history)
]
