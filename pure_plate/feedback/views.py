import json

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
from .models import Restaurant, Feedback
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@api_view(['POST'])
@csrf_exempt
@permission_classes([AllowAny])
def createFeedback(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except ValueError as e:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
        restaurant_name = data.get('restaurant_name')
        restaurant = get_object_or_404(Restaurant, name=restaurant_name)
        
        Feedback.objects.create(
            restaurant=restaurant,
            vegan=data.get('vegan') == 'true',
            halal=data.get('halal') == 'true',
            gluten_free=data.get('gluten_free') == 'true',
            lacto_free=data.get('lacto_free') == 'true',
            comments=data.get('comments')
        )

        return JsonResponse({'message': 'Feedback submitted successfully'}, status=201)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)
