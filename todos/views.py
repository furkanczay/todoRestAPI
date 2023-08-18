from django.shortcuts import render
from rest_framework import generics
from .models import TodoModel, User
from .serializers import TodoSerializer


class TodoListApiView(generics.ListAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer


class TodoDetailApiView(generics.RetrieveAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'


class TodoCreateApiView(generics.CreateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer


class TodoUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'


class TodoDestroyApiView(generics.RetrieveDestroyAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'
