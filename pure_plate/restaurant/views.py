from django.http import JsonResponse
from django.db.models import Count, Q
from .models import Place, Category

def places_in_categories_view(request):

    category_names = request.GET.get('categories', '')
    category_names_list = category_names.split(',')

    if not category_names: #카테고리를 입력받지 않았을경우 모든 장소를 json으로 리턴
        places = Place.objects.all().distinct()

    else:
        # 입력받은 카테고리 이름에 해당하는 모든 place들을 찾음
        categories = Category.objects.filter(Categoryname__in=category_names_list).values_list('PlaceID', flat=True)

        places = Place.objects.filter(PlaceID__in=categories).annotate(num_categories=Count('category')).filter(num_categories=len(category_names_list))


    places_json = [{'PlaceID': place.PlaceID, 'Name': place.Name} for place in places]

    return JsonResponse({'places': places_json})