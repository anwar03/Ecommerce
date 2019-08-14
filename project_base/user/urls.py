from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path('register', views.UserRegistrationApiView.as_view(), name='register'),
    path('<int:pk>/profile', views.ProfileApiView.as_view(), name='profile'),
    path('login/', views.LoginApiView.as_view(), name='login'),
    path('logout/', views.LogoutApiView.as_view(), name='logout'),
    
]