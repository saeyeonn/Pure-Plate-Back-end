from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_favorites, name='add_favorites'),
    path('user/<int:user_id>/', views.get_favorites, name='get_favorites'),
    path('delete/', views.delete_favorites, name='delete_favorites'),
]
