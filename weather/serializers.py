from rest_framework.serializers import ModelSerializer
from .models import Weather

class WeatehrSerializer(ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'