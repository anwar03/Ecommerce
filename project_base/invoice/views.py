from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import AddInvoiceSerializer, InvoiceSerializer
from base.permissions import IsOwner
from .models import Invoice
from product.models import Product


class AddToCartApiView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = AddInvoiceSerializer

    def perform_create(self, serializer):
        serializer.validated_data['created_by'] = self.request.user
        serializer.validated_data['buyer'] = self.request.user
        
        return super(AddToCartApiView, self).perform_create(serializer)

class OrderListApiView(generics.ListAPIView):
    permission_classes = ( IsAuthenticated, )
    serializer_class  = InvoiceSerializer
    
    def get_queryset(self):
        if self.request.user.user_type == 'buyer':
            return Invoice.objects.filter(buyer=self.request.user.id, status='pending')
        
        if self.request.user.user_type == 'seller':
            return Invoice.objects.filter(seller=self.request.user.id)
        
        return Invoice.objects.none()

# class OrderApiView(generics.CreateAPIView):
    