from rest_framework import serializers
from .models import TodoModel
from users.serializers import UserSerializer


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoModel
        fields = '__all__'
