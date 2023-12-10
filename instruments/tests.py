from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework import status

class AuthenticationTests(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com',
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_authentication_endpoints(self):
        client = APIClient()

        response = client.post('/api/login/', {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)

        response = client.post('/api/login/', {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 401)
        self.assertIn('error', response.data)

    def test_custom_permissions(self):
        client = APIClient()

        user_data = {
            'username': 'regular_user',
            'password': 'regular_password',
            'email': 'regular@example.com',
        }
        regular_user = User.objects.create_user(**user_data)
        client.force_authenticate(user=regular_user)

        response = client.get('/your/admin/endpoint/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        admin_data = {
            'username': 'admin_user',
            'password': 'admin_password',
            'email': 'admin@example.com',
            'is_staff': True,
        }
        admin_user = User.objects.create_user(**admin_data)
        client.force_authenticate(user=admin_user)

        response = client.get('/your/admin/endpoint/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_serializer_validations(self):
        client = APIClient()

        response = client.post('/api/register/', {'username': 'newuser', 'password': 'newpassword', 'email': 'new@example.com'})
        self.assertEqual(response.status_code, 201)

        response = client.post('/api/register/', {'username': 'testuser', 'password': 'newpassword', 'email': 'new@example.com'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('non_field_errors', response.data)
