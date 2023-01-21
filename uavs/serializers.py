from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Uav, UavCategory, UavCompany, UavBrand


class UavCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = UavCompany
        fields = ("id", "name")


class UavBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = UavBrand
        fields = ("id", "name", "company")


class UavCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UavCategory
        fields = ("id", "name")


class UavSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source="creator.username")
    company = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        slug_field="name",
        queryset=UavCompany.objects.all(),
    )
    brand = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        slug_field="name",
        queryset=UavBrand.objects.all(),
    )
    category = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        slug_field="name",
        queryset=UavCategory.objects.all(),
    )

    class Meta:
        model = Uav
        fields = ("id", "name", "year", "creator", "company", "brand", "category")
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    uavs = serializers.PrimaryKeyRelatedField(many=True, queryset=Uav.objects.all())

    class Meta:
        model = User
        fields = ("id", "username", "uavs")
