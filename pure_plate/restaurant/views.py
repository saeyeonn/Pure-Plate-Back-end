from django.http import JsonResponse
from django.db.models import Count
from .models import Restaurant, Category

def restaurant_in_categories_view(request):
    try:
        category_names = request.GET.get('categories', '')
        if not category_names:  
            return JsonResponse({
                'status': 200,
                'message': 'Category is not selected.',
                'data': []
            })

        category_names_list = category_names.split(',')

        # find all restaurants in selected categories
        categories = Category.objects.filter(CategoryName__in=category_names_list)
        restaurants = Restaurant.objects.filter(categories__in=categories).distinct()

        # filtered restaurants list category by category
        data = {}
        for category_name in category_names_list:
            category_restaurants = restaurants.filter(categories__CategoryName=category_name)
            category_list = [{
                'restaurantId': restaurant.RestaurantID,
                'restaurantName': restaurant.Name,
                'restaurantAddress': restaurant.Address,
                'restaurantLatitude': restaurant.Latitude,
                'restaurantLongitude': restaurant.Longitude,
                'restaurantReviewCount': restaurant.reviewCount,
                'restaurantRating': str(restaurant.avgRating),
            } for restaurant in category_restaurants]
            data[f"{category_name}List"] = category_list

        response = {
            'status': 200,
            'message': 'Successfully retrieved the restaurant list.',
            'data': [data]
        }

        return JsonResponse(response)

    except Exception as e:
        return JsonResponse({'status': 400, 'message': str(e), 'data': []})
