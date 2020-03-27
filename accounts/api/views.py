from rest_framework.views import APIView # access to the api view master class
from .serializers import * # access to all the serializers
from django.shortcuts import get_object_or_404
from django.contrib.auth import (
login as django_login,
logout as django_logout
) # access to the django login logout functions for same very purpose
from rest_framework.authtoken.models import Token # access to token for auth token assignment on login
from rest_framework.response import Response # access to the api response class
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication # access to authentication classes
from rest_framework.viewsets import (
ModelViewSet, ReadOnlyModelViewSet
) # access to viewset models
from rest_framework.mixins import (
ListModelMixin, CreateModelMixin, DestroyModelMixin,
RetrieveModelMixin, UpdateModelMixin,
)
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import (
IsAuthenticated,IsAuthenticatedOrReadOnly
) # access to the built-in permission classes
from .permissions import * # access to custom permission classes
from rest_framework.decorators import action # access to the some decorator functions

class UserProfileViewset(ReadOnlyModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = Profile.objects.filter(user__is_active=True)
    def get_serializer_class(self):
        if self.action=='list':
            return UserProfileListSerializer
        else:
            return UserProfileSerializer
    def update(self, request, *args, **kwargs):
        return ModelViewSet.update(self, request, *args, **kwargs)
    def get_permissions(self):
        if self.action=='list':
            permission_classes = [IsAuthenticatedOrReadOnly(),]
        else:
            permission_classes = [IsOwnerOrReadOnly(),]
        return permission_classes
   
class GetUserProfile(APIView):
    # serializer_class = UserProfileUpdateSerializer
    # queryset=Image.objects.all()
    lookup_field='id'
    permission_classes = [IsOwnerOrSuperUserOrReadOnly]
    def get(self, request):
        if not request.user.is_authenticated:
            return Response({'details':'you are not logged in'}, status=300)
        profile = request.user.profile
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data, status=200)

    def put(self, request):
        if not request.user.is_authenticated:
            return Response({'details':'you are not logged in'}, status=300)
        profile = request.user.profile
        serializer = UserProfileUpdateSerializer(data=request.data, instance=profile)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=200)

    def patch(self, request):
        if not request.user.is_authenticated:
            return Response({'details':'you are not logged in'}, status=300)
        profile = request.user.profile
        serializer = UserProfileUpdateSerializer(data=request.data, instance=profile)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=200)


class GetUserDetails(APIView):
    def get(self, request, id=None):
        user = get_object_or_404(User, id=id)
        profile = Profile.objects.get(user=user)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data, status=200)


class LoginView(APIView):
    """
    This class does not check for somethings to log someone in an alternative
    is to use django rest auth login api view or make a custom api view that puts
    that into consideration
    """
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token":token.key}, status=200)

class LogoutView(APIView):
    authentication_classes = [TokenAuthentication,]
    def post(self,request):
        django_logout(request)
        return Response({"details":"successfully logged out"}, status=200)
