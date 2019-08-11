from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import LoginViewsetApiView, UserRegistrationApiView, ProfileApiView

router = DefaultRouter()

router.register('login', LoginViewsetApiView, base_name='login')

urlpatterns = [
    path('register', UserRegistrationApiView.as_view(), name='register'),
    path('<int:pk>/profile', ProfileApiView.as_view(), name='profile'),
    path('', include(router.urls)),
]