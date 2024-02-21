from django.urls import path
from .views import hello_world, hotel_list

app_name = 'main'

urlpatterns = [
  path('hello/', hello_world, name="greating"),
  path('hotels/', hotel_list, name="hotels"),
]