from django.urls import path

from .views import DogReservationViewSet

urlpatterns = [
    path('dog-reservations', DogReservationViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('dog-reservations/<str:pk>', DogReservationViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]
