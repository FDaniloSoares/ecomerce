from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

User = get_user_model()


class AccountTests(APITestCase):
    def test_create_user(self):
        url = reverse("account:create-user")
        data = {"name": "John Tester", "username": "john", "password": "123"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, data["name"])
        self.assertEqual(User.objects.get().username, data["username"])
        self.assertTrue(Token.objects.get(user__username=data["username"]))
