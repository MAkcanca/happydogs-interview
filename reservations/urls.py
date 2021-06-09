from django.urls import path

from .views import DogReservationViewSet, DogCreateView

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
    path('dogs/', DogCreateView.as_view())
]
