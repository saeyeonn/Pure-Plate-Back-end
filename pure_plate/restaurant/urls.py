from django.contrib import admin
from django.urls import path

from . import views



urlpatterns = [
    path('places/',views.places_in_categories_view, name='places-in-categories')
]