from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Favorite
from restaurant.models import Restaurant
from account.models import User

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_favorites(request, restaurant_name):
    user = request.user
    try:
        restaurant = Restaurant.objects.get(name=restaurant_name)
        favorite, created = Favorite.objects.get_or_create(user=user, restaurant=restaurant)
        if created:
            return Response({'message': 'Restaurant added to favorites successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Restaurant is already in favorites'}, status=status.HTTP_200_OK)
    except Restaurant.DoesNotExist:
        return Response({'error': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_favorites(request):
    user = request.user
    favorites = Favorite.objects.filter(user=user)
    favorite_restaurants = [{'restaurant_id': favorite.restaurant.id, 'restaurant_name': favorite.restaurant.name} for favorite in favorites]
    return Response({'favorites': favorite_restaurants}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_favorites(request, restaurant_name):
    user = request.user
    try:
        restaurant = Restaurant.objects.get(name=restaurant_name)
        favorite = Favorite.objects.filter(user=user, restaurant=restaurant)
        if favorite.exists():
            favorite.delete()
            return Response({'message': 'Restaurant removed from favorites successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Restaurant is not in favorites'}, status=status.HTTP_404_NOT_FOUND)
    except Restaurant.DoesNotExist:
        return Response({'error': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)
