from django.urls import path
from .views import home, f, createuser

urlpatterns = [
    path('home', home, name='base-home'),
    path('register', f, name='register'),
    path('createuser', createuser, name='user'),
]
