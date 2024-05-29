from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.createFeedback, name='submit_feedback'),  
]

