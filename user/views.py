from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from rest_framework import generics

from .serializers import UserRegistrationSerializer, ProfileSerializer
from .models import User

class UserRegistrationApiView(generics.CreateAPIView):
    """User registration api view."""

    serializer_class = UserRegistrationSerializer


class LoginViewsetApiView(viewsets.ViewSet):
    """Checks username and password is valid return Authentication token"""
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """using ObtainAuthToken Return token for after login user."""

        return ObtainAuthToken().post(request)
    
    
class ProfileApiView(generics.RetrieveAPIView):
    
    permission_classes = ( IsAuthenticatedOrReadOnly, )
    serializer_class = ProfileSerializer
    
    def get_queryset(self):
        profile = User.objects.get(id=self.kwargs['pk'])
        return profile
    