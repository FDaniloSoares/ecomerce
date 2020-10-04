from apps.product.models import Categoria, Produto
from rest_framework import serializers

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ["id", "name"]

class ProdutoSerializer(serializers.ModelSerializer):
    category = CategoriaSerializer()

    class Meta:
        model = Produto
        fields = ["id", "name", "description", "price", "category", "image" ]