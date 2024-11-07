from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from books.serializers import FavoriteSerializer
from .models import User

class RegisterUserSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True, 
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  username = serializers.CharField(
    required=True, 
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

  class Meta:
    model = User
    fields = ['email', 'password', 'username']
    extra_kwargs = {
      'password': {'write_only': True, 'min_length': 3},
    }
    
  def create(self, validated_data):
    user = self.Meta.model.objects.create(
      email=validated_data['email'],
      username=validated_data['username'],
    )

    user.set_password(validated_data['password'])
    user.save()

    return user
  
class ProfileSerializer(serializers.ModelSerializer):
   favorites = FavoriteSerializer(many = True, read_only=True)

   class Meta:
      model = User
      fields = ['id', 'username', 'email', 'favorites']