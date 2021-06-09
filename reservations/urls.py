from django.urls import path

from .views import DogReservationViewSet, DogCreateView, fill_test_data

urlpatterns = [
    path('dog-reservations', DogReservationViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name="dog-reservation"),
    path('dog-reservations/<str:pk>', DogReservationViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('dogs/', DogCreateView.as_view(), name="dog"),
    path('test-data/', fill_test_data)
]
