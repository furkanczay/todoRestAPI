from rest_framework import serializers
from django.contrib.auth.models import User, Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = 'permissions'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password', 'user_permissions')
