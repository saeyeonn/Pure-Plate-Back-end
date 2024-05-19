from django.http import JsonResponse
from django.db.models import Count
from .models import Place, Category

def places_in_categories_view(request):
    try:
        category_names = request.GET.get('categories', '')
        if not category_names:  # 카테고리를 입력받지 않았을 경우 빈 목록을 반환
            places_json = []
        else:
            category_names_list = category_names.split(',')

            # 입력받은 카테고리 이름에 해당하는 모든 Place들을 찾음
            categories = Category.objects.filter(CategoryName__in=category_names_list)
            places = Place.objects.filter(categories__in=categories).distinct()

            # 입력받은 모든 카테고리에 속한 Place들을 찾기 위해 그룹화 및 개수 필터 적용
            places = places.annotate(num_categories=Count('categories')).filter(num_categories=len(category_names_list))

            places_json = [{'PlaceID': place.PlaceID, 'Name': place.Name} for place in places]

        return JsonResponse({'places': places_json})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
