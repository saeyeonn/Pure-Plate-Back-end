from django.http import JsonResponse
from django.db.models import Count
from .models import Place, Category

def places_in_categories_view(request):
    try:
        category_names = request.GET.get('categories', '')
        if not category_names:  
            return JsonResponse({
                'status': 200,
                'message': 'Category is not selected.',
                'data': []
            })

        category_names_list = category_names.split(',')

        # find all places in selected categories
        categories = Category.objects.filter(CategoryName__in=category_names_list)
        places = Place.objects.filter(categories__in=categories).distinct()

        # filtered restaurants list category by category
        data = {}
        for category_name in category_names_list:
            category_places = places.filter(categories__CategoryName=category_name)
            category_list = [{
                'restaurantId': place.PlaceID,
                'restaurantName': place.Name,
                'restaurantAddress': place.Address,
                'restaurantLatitude': str(place.Latitude),
                'restaurantLongitude': str(place.Longitude),
                'restaurantReviewCount': place.reviewCount,
                'restaurantRating': str(place.avgRating),
            } for place in category_places]
            data[f"{category_name}List"] = category_list

        response = {
            'status': 200,
            'message': 'Successfully retrieved the restaurant list.',
            'data': [data]
        }

        return JsonResponse(response)

    except Exception as e:
        return JsonResponse({'status': 400, 'message': str(e), 'data': []})
