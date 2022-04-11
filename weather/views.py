from os import stat
import requests
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Weather
from .serializers import WeatehrSerializer
from rest_framework.pagination import PageNumberPagination
import logging


logging.basicConfig(filename='logs.txt',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.INFO)


@api_view(['GET'])
def weather(request, city_name):
    API_key = "949d4bb2791c644c86becf63534aaae6"
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"
    response = requests.get(api_url)
    data = response.json()
    if response.status_code == 200:
        Weather.objects.create(data=data)
        logging.info("new weather entry")
        return Response(data, status=status.HTTP_200_OK)
    else:
        logging.error('error while getting weather data')
        return Response({'details': 'city is not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def weather_history(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    qs = Weather.objects.all()
    result = paginator.paginate_queryset(qs, request)
    serailizer = WeatehrSerializer(result, many=True)
    logging.info('listing history of weater')
    return paginator.get_paginated_response(serailizer.data)
