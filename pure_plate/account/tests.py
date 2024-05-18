from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginLogoutAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', email='test@example.com', password='test123')


    def test_login(self):
        url = reverse('login')
        data = {'email': 'test@example.com', 'password': 'test123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_logout(self):
        url = reverse('logout')
        self.client.login(email='test@example.com', password='test123')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
