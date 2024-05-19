from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import Review
from account.models import User
from restaurant.models import Restaurant

@api_view(['POST'])
@csrf_exempt
def review(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        restaurant_id = request.POST.get('restaurant_id')
        rating = request.POST.get('rating')
        review_text = request.POST.get('review_text')
        visit_date = request.POST.get('visit_date')  

        # validation
        if not all([user_id, restaurant_id, rating, review_text, visit_date]):
            return JsonResponse({'error': 'Missing required fields'}, status=400)

        try:
            # validate existance
            user = User.objects.get(pk=user_id)
            restaurant = Restaurant.objects.get(pk=restaurant_id)
        except (User.DoesNotExist, Restaurant.DoesNotExist):
            return JsonResponse({'error': 'User or restaurant not found'}, status=404)

        review = Review.objects.create(
            User=user,
            Restaurant=restaurant,
            Rating=rating,
            ReviewText=review_text,
            VisitDate=visit_date
        )

        return JsonResponse({'message': 'Review created successfully'}, status=201)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)