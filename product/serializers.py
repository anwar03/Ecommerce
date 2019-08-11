from rest_framework import serializers
from .models import Product


class AddProductSerializer(serializers.ModelSerializer):
    """Add Product Serializer."""

    class Meta:
        model = Product
        fields = ['image', 'name', 'description', 'amount_of_quantites', 'unit_price']
        
    def validate(self, data):
        if self.context['request'].user.user_type == 'buyer' :
            raise serializers.ValidationError({"message" : "Buyer can not add product"})
        
        return data
        

class ProductSerializer(serializers.ModelSerializer):
    """Product Serializer."""

    class Meta:
        model = Product
        fields = ['id', 'image', 'name', 'description', 'amount_of_quantites', 'unit_price', 'seller']
