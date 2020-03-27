from rest_framework import serializers
from accounts.models import *
from rest_framework import exceptions
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['number', 'country_code']

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = User
        fields= ('username', 'email', 'first_name', 'last_name')

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('username', 'email', 'first_name', 'last_name')

class UserProfileListSerializer(serializers.ModelSerializer):
    """
    This serializer is only for viewing the creating is not included
    """
    user = UserSerializer()
    class Meta:
        model = Profile
        fields= ('user', 'reference_id')
        read_only_fields = ('user',)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields= "__all__"
        read_only_fields = ('reference_id',)
        depth=3

class UserProfileUpdateSerializer(serializers.ModelSerializer):
    phone = ContactSerializer(required=False)
    class Meta:
        model = Profile
        fields= "__all__"
        read_only_fields = ('reference_id',)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    def validate(self, data):
        username = data.get('username', '')
        password = data.get('password', '')
        if password and username:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    raise exceptions.ValidationError('account is disabled')
            else:
                raise exceptions.ValidationError('the user name and password can not be found in the database')

        else:
            raise exceptions.ValidationError('You can not login without username and password')
        return data

class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password", "confirm_password")
