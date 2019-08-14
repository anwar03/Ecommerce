from django.urls import path, include

from . import views

urlpatterns = [
    path('add', views.AddToCartApiView.as_view(), name='add-invoice'),
    path('order_list', views.OrderListApiView.as_view(), name='order-list'),
    path('order', views.OrderApiView.as_view(), name='order'),
]
