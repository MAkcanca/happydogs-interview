from rest_framework import serializers
from .models import Dog
from .models import DogReservation


class DogReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DogReservation
        fields = '__all__'


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'

    def create(self, validated_data):
        dog, created = Dog.objects.get_or_create(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name', None)
        )

        return dog
