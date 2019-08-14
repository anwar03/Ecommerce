from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import status

from .serializers import UserRegistrationSerializer, ProfileSerializer, LoginSerializer
from .models import User
from base.permissions import ProfilePermission

from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from rest_framework.views import APIView

class UserRegistrationApiView(generics.CreateAPIView):
    """User registration api view."""

    serializer_class = UserRegistrationSerializer


# class LoginViewsetApiView(viewsets.ViewSet):
#     """Checks username and password is valid return Authentication token"""
#     serializer_class = AuthTokenSerializer
#     authentication_classes = ( TokenAuthentication, )

#     def create(self, request):
#         """using ObtainAuthToken Return token for after login user."""

#         return ObtainAuthToken().post(request)
    
 
class LoginApiView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_200_OK)
    
class LogoutApiView(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class ProfileApiView(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = ( IsAuthenticatedOrReadOnly, ProfilePermission, )
    serializer_class = ProfileSerializer
    
    def get_queryset(self):
        profile = User.objects.filter(id=self.kwargs.get('pk'))
        return profile