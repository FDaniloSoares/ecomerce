from apps.product.models import Categoria, Produto
from apps.product.serializers import CategoriaSerializer, ProdutoSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]


class ProdutoViewSet(viewsets.ModelViewSet):
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["name"]
    filterset_fields = ["name"]
