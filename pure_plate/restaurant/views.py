from django.http import JsonResponse
from django.db.models import Count
from .models import Restaurant

#/api/restaurants_in_categories?categories=Italian,Chinese,Mexican

def restaurants_in_categories_view(request):

    try:
        category_names = request.GET.get('categories', '')
        if not category_names:  
            return JsonResponse({
                'status': 200,
                'message': 'Category is not selected.',
                'data': []
            })

        category_names_list = category_names.split(',')

        filter_conditions = {}
        if 'vegan' in category_names_list:
            filter_conditions['vegan'] = True
        if 'halal' in category_names_list:
            filter_conditions['halal'] = True
        if 'glutenfree' in category_names_list:
            filter_conditions['gluten_free'] = True
        if 'lactofree' in category_names_list:
            filter_conditions['lacto_free'] = True

        restaurants = Restaurant.objects.filter(**filter_conditions)


        data = [{
            'restaurantId': restaurant.id,
            'restaurantName': restaurant.name,
            'restaurantAddress': restaurant.address,
            'restaurantLatitude': str(restaurant.latitude),
            'restaurantLongitude': str(restaurant.longitude),
            'restaurantTime': restaurant.time,
            'restaurantPhoto': restaurant.photo,
            'restaurantPhone': restaurant.phone,
            'restaurantReviewCount': restaurant.review_count,
            'restaurantRating': str(restaurant.avg_rating),
            'restaurantVegan': restaurant.vegan,
            'restaurantHalal': restaurant.halal,
            'restaurantGlutenFree': restaurant.gluten_free,
            'restaurantLactoFree': restaurant.lacto_free
        } for restaurant in restaurants]


        response = {
            'status': 200,
            'message': 'Successfully retrieved the restaurant list.',
            'data': data
        }

        return JsonResponse(response)

    except Exception as e:
        return JsonResponse({'status': 400, 'message': str(e), 'data': []})



