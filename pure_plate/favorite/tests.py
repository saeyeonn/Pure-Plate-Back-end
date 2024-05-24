from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Favorite
from account.models import User
from restaurant.models import Restaurant
import random

class FavoriteAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='test@example.com', password='testpassword')
        self.latitude = random.uniform(-90, 90)
        self.longitude = random.uniform(-180, 180)
        self.restaurant = Restaurant.objects.create(name='Test Restaurant', latitude=self.latitude, longitude=self.longitude)

    def test_add_favorite(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('add_favorites')
        response = self.client.post(url, {'user_id': self.user.id, 'restaurant_id': self.restaurant.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Favorite.objects.filter(user=self.user, restaurant=self.restaurant).count(), 1)

    def test_get_user_favorites(self):
        self.client.force_authenticate(user=self.user)
        Favorite.objects.create(user=self.user, restaurant=self.restaurant)
        response = self.client.get(reverse('get_favorites', kwargs={'user_id': self.user.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['favorites'][0]['restaurant_id'], self.restaurant.id)

    def test_remove_favorite(self):
        self.client.force_authenticate(user=self.user)
        Favorite.objects.create(user=self.user, restaurant=self.restaurant)
        response = self.client.post(reverse('delete_favorites'), {'user_id': self.user.id, 'restaurant_id': self.restaurant.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Favorite.objects.filter(user=self.user, restaurant=self.restaurant).count(), 0)

