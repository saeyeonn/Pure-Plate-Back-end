from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class AccountTests(APITestCase):
    def test_register_user(self):
        url = reverse('register')
        data = {'name': 'test', 'email': 'test@example.com', 'password': 'password123'}
        response = self.client.post(url, data, format='json')  # POST 요청
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
