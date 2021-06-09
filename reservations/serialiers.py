from rest_framework import serializers
from .models import Dog
from .models import DogReservation


class DogReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DogReservation
        fields = '__all__'
