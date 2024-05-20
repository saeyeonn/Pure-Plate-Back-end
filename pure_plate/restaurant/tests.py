

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .models import Restaurant, Category

class RestaurantCategoryTest(TestCase):
    def setUp(self):
        # 테스트에 사용할 카테고리와 식당 생성
        category1 = Category.objects.create(category_name="한식")
        category2 = Category.objects.create(category_name="중식")
        
        restaurant1 = Restaurant.objects.create(
            name="한식당",
            address="서울시 강남구",
            latitude="37.517235",
            longitude="127.047325",
            review_count=10,
            avg_rating=4.5
        )
        restaurant2 = Restaurant.objects.create(
            name="중식당",
            address="서울시 서초구",
            latitude="37.517235",
            longitude="127.047325",
            review_count=5,
            avg_rating=4.0
        )

        # 생성한 식당을 각각의 카테고리에 할당
        restaurant1.categories.add(category1)
        restaurant2.categories.add(category2)

    def test_restaurants_in_categories(self):
        # 카테고리를 기준으로 식당 목록을 요청하는 URL
        url = reverse('restaurants_in_categories_view') + '?categories=한식,중식'
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
        # 응답 데이터 검증
        data = response.json()
        self.assertEqual(data['status'], 200)
        self.assertIn('한식List', data['data'][0])
        self.assertIn('중식List', data['data'][0])
        self.assertEqual(len(data['data'][0]['한식List']), 1)
        self.assertEqual(len(data['data'][0]['중식List']), 1)
        self.assertEqual(data['data'][0]['한식List'][0]['restaurantName'], "한식당")
        self.assertEqual(data['data'][0]['중식List'][0]['restaurantName'], "중식당")

