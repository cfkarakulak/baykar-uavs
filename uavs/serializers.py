from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Uav


class UavSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Uav
        fields = ('id', 'title', 'genre', 'year', 'creator', 'company', 'brand', 'category')
        depth = 1


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    uavs = serializers.PrimaryKeyRelatedField(many=True, queryset=Uav.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'uavs')
