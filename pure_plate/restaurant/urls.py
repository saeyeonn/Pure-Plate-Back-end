from django.contrib import admin
from django.urls import path, include

from . import views



urlpatterns = [
    path('restaurant/', views.restaurants_in_categories_view, name='restaurants_in_categories_view')
]