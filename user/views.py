from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView

from .serializers import UserRegistrationSerializer


class UserRegistrationApiView(CreateAPIView):
    """User registration api view."""

    serializer_class = UserRegistrationSerializer


class LoginViewsetApiView(viewsets.ViewSet):
    """Checks username and password is valid return Authentication token"""
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """using ObtainAuthToken Return token for after login user."""

        return ObtainAuthToken().post(request)