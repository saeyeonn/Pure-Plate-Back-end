from rest_framework import serializers
from .models import User
from django.contrib.auth.models import update_last_login
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user




class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise serializers.ValidationError('Unable to log in with provided credentials.')

            data['user'] = user
            return data
        else:
            raise serializers.ValidationError('Must include "email" and "password".')
