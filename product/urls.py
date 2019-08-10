from django.urls import path, include

from . import views

urlpatterns = [
    path('add', views.AddProductApiView.as_view(), name='add-product'),
    path('list', views.ProductListApiViewForAll.as_view(), name='all-product-list'),
    path('seller_product_list', views.ProductListApiViewForSeller.as_view(), name='seller-product-list'),
    path('product_details/<int:pk>/', views.ProductDetailsApiView.as_view(), name='product-details'),
]