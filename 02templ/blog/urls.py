from django.urls import path
from .views import home, room

urlpatterns = [
    path('home/', home),
    path('room/', room)
]
