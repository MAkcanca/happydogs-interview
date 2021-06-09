# from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from .models import DogReservation, Dog
from .serialiers import DogReservationSerializer, DogSerializer


# Consider using APIViews
class DogReservationViewSet(viewsets.ViewSet):
    def list(self, request):
        reservations = DogReservation.objects.all()
        serializer = DogReservationSerializer(reservations, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = DogReservationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if(serializer.validated_data.get("start_date") > serializer.validated_data.get("end_date")):
            raise APIException("Date's are incorrect")
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        reservation = DogReservation.objects.get(id=pk)
        serializer = DogReservationSerializer(reservation)
        return Response(serializer.data)

    def update(self, request, pk=None):
        reservation = DogReservation.objects.get(id=pk)
        serializer = DogReservationSerializer(
            instance=reservation, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        reservation = DogReservation.objects.get(id=pk)
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DogCreateView(generics.CreateAPIView):
    serializer_class = DogSerializer
