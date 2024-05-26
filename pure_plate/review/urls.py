from django.urls import path
from . import views

urlpatterns = [
    path('enroll/', views.review, name='enroll_review'),
    path('view/', views.reviews_list, name='view_review'),    
]

