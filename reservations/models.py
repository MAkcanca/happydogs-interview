from django.db import models


class Dog(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(
        max_length=200, null=True, blank=True)  # Optional

    def name(self):
        return self.__str__()

    def __str__(self):
        return self.first_name + " " + self.last_name


class DogReservation(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return str(self.dog) + " " + str(self.start_date)
