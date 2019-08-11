from rest_framework import serializers

from .models import Invoice
from product.models import Product
from user.serializers import ProfileSerializer

class AddInvoiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Invoice
        fields = ['product', 'seller', 'amount_of_quantities', 'cost']
        read_only_fields = ('cost', )
    
    
    def validate(self, data):
        amount_of_quantities = data['amount_of_quantities']
        product_id = data['product']    
        product = Product.objects.get(name=product_id)
        product_price = product.unit_price
        cost = product_price * amount_of_quantities
        data['cost'] = cost
        data['status'] = 'pending'
        data['unit_price'] = product_price
        
        if product.amount_of_quantites < 1 :
            raise serializers.ValidationError({"message" : "Product is not avaiable."})
        if product.amount_of_quantites < amount_of_quantities:
            raise serializers.ValidationError({"message": "'%s' Product are not avaiable." % amount_of_quantities})
        
        return data
    

class InvoiceSerializer(serializers.ModelSerializer):
    
    seller = ProfileSerializer()
    buyer = ProfileSerializer()
    
    class Meta:
        model = Invoice
        fields = ['id', 'product', 'amount_of_quantities', 'unit_price', 'cost', 'seller', 'buyer']