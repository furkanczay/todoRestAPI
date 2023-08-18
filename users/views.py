from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, GroupSerializer


class UserListApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailApiView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'


class GroupListApiView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

