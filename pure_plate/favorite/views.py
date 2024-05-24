
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Favorite
from restaurant.models import Restaurant
from account.models import User


@api_view(['POST'])
@permission_classes([AllowAny])
def add_favorites(request):
    user_id = request.data.get('user_id')
    restaurant_id = request.data.get('restaurant_id')
    if not user_id or not restaurant_id:
        return Response({'error': 'User ID and restaurant ID are required'}, status=400)
    try:
        user = User.objects.get(pk=user_id)
        restaurant = Restaurant.objects.get(pk=restaurant_id)
        favorite, created = Favorite.objects.get_or_create(user=user, restaurant=restaurant)
        if created:
            return Response({'message': 'Restaurant added to favorites successfully'}, status=201)
        else:
            return Response({'message': 'Restaurant is already in favorites'}, status=200)
    except (User.DoesNotExist, Restaurant.DoesNotExist):
        return Response({'error': 'User or restaurant not found'}, status=404)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_favorites(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        favorites = Favorite.objects.filter(user=user)
        favorite_restaurants = [{'restaurant_id': favorite.restaurant.id, 'restaurant_name': favorite.restaurant.name} for favorite in favorites]
        return Response({'favorites': favorite_restaurants})
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)

@api_view(['POST'])
@permission_classes([AllowAny])
def delete_favorites(request):
    user_id = request.data.get('user_id')
    restaurant_id = request.data.get('restaurant_id')
    if not user_id or not restaurant_id:
        return Response({'error': 'User ID and restaurant ID are required'}, status=400)
    try:
        user = User.objects.get(pk=user_id)
        restaurant = Restaurant.objects.get(pk=restaurant_id)
        favorite = Favorite.objects.filter(user=user, restaurant=restaurant)
        if favorite.exists():
            favorite.delete()
            return Response({'message': 'Restaurant removed from favorites successfully'}, status=200)
        else:
            return Response({'error': 'Restaurant is not in favorites'}, status=404)
    except (User.DoesNotExist, Restaurant.DoesNotExist):
        return Response({'error': 'User or restaurant not found'}, status=404)

