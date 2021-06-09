from rest_framework import serializers
from .models import Dog
from .models import DogReservation


class DogReservationSerializer(serializers.ModelSerializer):
    dog_name = serializers.CharField(source='dog', read_only=True)

    class Meta:
        model = DogReservation
        fields = ('id', 'start_date', 'end_date', 'dog_name', 'dog')


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
