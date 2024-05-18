from django.contrib import admin
from django.urls import path
from .views import places_in_categories_view


urlpatterns = [
    path('places/',places_in_categories_view, name='places-in-categories')
]