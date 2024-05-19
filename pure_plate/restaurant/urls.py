from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('restaurants/',views.restaurants_in_categories_view, name='restaurants-in-categories')
]