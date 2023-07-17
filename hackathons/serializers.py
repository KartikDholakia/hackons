from rest_framework import serializers
from .models import Hackathon
from django.contrib.auth.models import User


class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = '__all__'


class SignupSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    # check if this user is already in our database:
    def validate(self, data):
        if data['email']:
            if User.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError('User already exists!')
            
        return data
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()

        return user
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

