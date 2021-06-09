from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from .models import Dog, DogReservation


class DogTests(APITestCase):
    def test_dog_reservation(self):
        """
        Ensure we can create a new dog object.
        """
        data = {
            'first_name': 'Peanut',
            'last_name': 'Butter'
        }
        url = reverse('dog')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Dog.objects.count(), 1)
        self.assertEqual(Dog.objects.get().first_name, 'Peanut')


class DogReservationTests(APITestCase):
    def setUp(self):
        Dog.objects.create(first_name="Peanut", last_name="Butter")

    def test_dog_reservation(self):
        """
        Ensure we can create a new dog reservation object.
        """
        data = {
            'start_date': '2021-05-05',
            'end_date': '2021-05-06',
            'dog': 1
        }
        url = reverse('dog-reservation')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DogReservation.objects.count(), 1)
        self.assertEqual(DogReservation.objects.get().dog.first_name, 'Peanut')

    def test_dog_reservation_dates(self):
        """
        Ensure dog reservation object doesn't allow start > end.
        """
        data = {
            'start_date': '2021-05-06',
            'end_date': '2021-05-05',
            'dog': 1
        }
        url = reverse('dog-reservation')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)
        self.assertEqual(DogReservation.objects.count(), 0)
