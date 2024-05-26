from django.test import TestCase, Client
from django.urls import reverse
from .models import Restaurant

class RestaurantSearchTests(TestCase):
    def setUp(self):
        self.client = Client()
        # 테스트를 위한 레스토랑 데이터를 생성합니다.
        Restaurant.objects.create(
            name='Vegan Bliss', address='123 Green Way', vegan=True, halal=False,
            gluten_free=True, lacto_free=False, latitude=10.0, longitude=20.0,
            time='09:00-21:00', photo='vegan_bliss.jpg', phone='111-222-3333',
            review_count=100, avg_rating=4.8
        )
        Restaurant.objects.create(
            name='Halal Heaven', address='456 Crescent Moon', vegan=False, halal=True,
            gluten_free=False, lacto_free=True, latitude=30.0, longitude=40.0,
            time='10:00-22:00', photo='halal_heaven.jpg', phone='444-555-6666',
            review_count=80, avg_rating=4.6
        )

    def test_search_for_vegan_restaurants(self):
        # 비건 옵션을 선택했을 때 해당하는 레스토랑이 반환되는지 테스트합니다.
        response = self.client.get(reverse('restaurants-in-categories'), {'categories': 'vegan'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Vegan Bliss', response.content.decode())

    def test_search_for_halal_restaurants(self):
        # 할랄 옵션을 선택했을 때 해당하는 레스토랑이 반환되는지 테스트합니다.
        response = self.client.get(reverse('restaurants-in-categories'), {'categories': 'halal'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Halal Heaven', response.content.decode())

    def test_search_for_gluten_free_and_lacto_free_restaurants(self):
        # 글루텐 프리와 락토 프리 옵션을 모두 선택했을 때 해당하는 레스토랑이 없다는 것을 테스트합니다.
        response = self.client.get(reverse('restaurants-in-categories'), {'categories': 'glutenfree,lactofree'})
        self.assertEqual(response.status_code, 200)
        content = response.content.decode()
        # 이 부분은 실제 반환되는 내용에 따라 수정이 필요할 수 있습니다.
        self.assertTrue('No restaurants found' in content or '[]' in content)
