from rest_framework.serializers import ModelSerializer
from .models import User


class UserRegistrationSerializer(ModelSerializer):
    """User Registration Serializer."""

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'user_type']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'},
            }
        }
        
class ProfileSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'user_type']