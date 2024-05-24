# from django.test import TestCase
# from django.urls import reverse
# from rest_framework.test import APITestCase
# from rest_framework import status
# from django.contrib.auth import get_user_model

# class LoginLogoutAPITest(APITestCase):
#     def setUp(self):
#         self.user_data = {'name': 'test', 'email': 'test@example.com', 'password': 'testpassword123'}
#         self.user = get_user_model().objects.create_user(email=self.user_data['email'], password=self.user_data['password'], name=self.user_data['name'])


#     def test_login(self):
#         url = reverse('login')
#         data = {'email': self.user_data['email'], 'password': self.user_data['password']}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('token', response.data)

#     def test_logout(self):
#         self.client.force_authenticate(user=self.user)
#         url = reverse('logout')
#         response = self.client.post(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
