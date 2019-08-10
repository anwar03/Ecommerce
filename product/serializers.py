from rest_framework.serializers import ModelSerializer
from .models import Product


class AddProductSerializer(ModelSerializer):
    """Add Product Serializer."""

    class Meta:
        model = Product
        fields = ['image', 'name', 'description', 'amount_of_quantites', 'unit_price']
        

class ProductSerializer(ModelSerializer):
    """Product Serializer."""

    class Meta:
        model = Product
        fields = ['id', 'image', 'name', 'description', 'amount_of_quantites', 'unit_price', 'seller']
