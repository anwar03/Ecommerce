from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated

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
    permission_classes = ( IsAuthenticatedOrReadOnly, )
    serializer_class  = ProductSerializer
    # queryset = Product.objects.all()
    
    def get_queryset(self):
        if self.request.user.user_type == 'seller':
            return Product.objects.filter(seller=self.request.user.id)
        return Product.objects.all()

# class ProductListApiViewForSeller(generics.ListAPIView):
#     permission_classes = ( IsAuthenticated, )
#     serializer_class  = ProductSerializer
    
#     def get_queryset(self):
#         if self.request.user:
#             return Product.objects.filter(seller=self.request.user)
#         return Product.objects.none()
    
class ProductDetailsApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = ( IsAuthenticated, IsOwner, )
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        queryset = Product.objects.filter(id=self.kwargs['pk'])
        return queryset
    