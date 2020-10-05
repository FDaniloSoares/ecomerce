from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.product.models import Categoria, Produto

User = get_user_model()


class ProductTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(name="Ubirani")
        cls.categoria = Categoria.objects.create(name="Infantil")
        cls.produto = Produto.objects.create(name="Carro", price="10.00")

    def test_crud_categoria(self):
        url = reverse("product:categorias-list")
        data = {"name": "Vestuario"}
        self.client.force_authenticate(user=self.user)

        # Create
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Categoria.objects.count(), 2)

        # Read
        url = f"http://localhost:8000/categorias/{self.categoria.id}/"
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Update
        data = {"name": "Vestuario Masculino"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], data["name"])

        # Delete
        response = self.client.delete(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_crud_produto(self):
        url = reverse("product:produtos-list")
        data = {"name": "Boneco Bira", "price": "1.99"}
        data2 = {"name": "Vestido Preto", "price": "99.99"}
        self.client.force_authenticate(user=self.user)

        # Create
        response = self.client.post(url, data, format="json")
        response = self.client.post(url, data2, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Produto.objects.count(), 3)

        # Read
        url = f"http://localhost:8000/produtos/{self.produto.id}/"
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Update
        data = {"price": "1.99"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["price"], data["price"])

        # Delete
        response = self.client.delete(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
