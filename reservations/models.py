from django.db import models


class Dog(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


class DogReservation(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
