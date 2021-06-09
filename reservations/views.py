# from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from django.http import JsonResponse

from .models import DogReservation, Dog
from .serializers import DogReservationSerializer, DogSerializer
from datetime import timedelta, date
from collections import namedtuple
import random
Range = namedtuple('Range', ['start', 'end'])

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
            raise APIException("Dates are incorrect")
        other_appointments = DogReservation.objects.filter(
            dog=serializer.validated_data.get("dog"))
        r1 = Range(start=serializer.validated_data.get("start_date"),
                   end=serializer.validated_data.get("end_date"))

        for appointment in other_appointments:
            r2 = Range(start=appointment.start_date, end=appointment.end_date)
            overlapping_days = min(
                r1.end - r2.start, r2.end - r1.start).days + 1
            if(overlapping_days > 0):
                raise APIException("Dates overlap")
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


def fill_test_data(request):
    Dog.objects.all().delete()
    dog = Dog(first_name='Peanut', last_name='Butter')
    dog.save()
    start_date = date.today()
    date_range = [start_date + timedelta(days=x) for x in range(30)]

    # Needs randomization
    for date_obj in date_range:
        res = DogReservation(start_date=date_obj, end_date=date_obj, dog=dog)
        res.save()
    return JsonResponse({"success": True})
