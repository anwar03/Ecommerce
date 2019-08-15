from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny

from .serializers import AddProductSerializer, ProductSerializer
from base.permissions import IsOwner
from .models import Product


class AddProductApiView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = AddProductSerializer

    def perform_create(self, serializer):
        serializer.validated_data['created_by'] = self.request.user
        serializer.validated_data['seller'] = self.request.user
        return super(AddProductApiView, self).perform_create(serializer)


class ProductListApiViewForAll(generics.ListAPIView):
    permission_classes = ( AllowAny, )
    serializer_class  = ProductSerializer
    
    def get_queryset(self):    
        if hasattr(self.request.user, 'user_type'):
            if self.request.user.user_type == 'seller':
                return Product.objects.filter(seller=self.request.user.id)
            
        return Product.objects.all()

class ProductDetailsApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = ( AllowAny, )
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        queryset = Product.objects.filter(id=self.kwargs['pk'])
        return queryset
