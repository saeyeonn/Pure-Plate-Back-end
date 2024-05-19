from django.test import TestCase
from django.contrib.auth import get_user_model
from restaurant.models import Restaurant, Category
from review.models import Review

class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            name='Test User',
            password='testpassword123'
        )
        self.category = Category.objects.create(category_name='Test Category')
        self.restaurant = Restaurant.objects.create(
            name='Test Restaurant',
            address='Test Address',
            latitude=0.0,
            longitude=0.0
        )
        self.restaurant.categories.add(self.category)

    def test_create_review(self):
        review = Review.objects.create(
            user=self.user,
            restaurant=self.restaurant,
            rating=4,
            review_text='This is a test review.',
            visit_date='2024-05-28'
        )

        self.assertEqual(review.user, self.user)
        self.assertEqual(review.restaurant, self.restaurant)
        self.assertEqual(review.rating, 4)
        self.assertEqual(review.review_text, 'This is a test review.')
        self.assertEqual(review.visit_date, '2024-05-28')

    def test_review_update_rating(self):
        initial_rating = self.restaurant.avg_rating
        # 리뷰를 생성하여 레스토랑의 평균 평점을 업데이트합니다.
        Review.objects.create(
            user=self.user,
            restaurant=self.restaurant,
            rating=5,
            review_text='Great restaurant!',
            visit_date='2024-05-28'
        )
        # 리뷰가 추가된 후의 레스토랑의 평균 평점이 이전과 다른지 확인합니다.
        updated_rating = Restaurant.objects.get(pk=self.restaurant.pk).avg_rating
        self.assertNotEqual(initial_rating, updated_rating)
