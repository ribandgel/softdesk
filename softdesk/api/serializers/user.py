from rest_framework import serializers

from softdesk.api.models import Contributor, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name")
        read_only_fields = ("id",)


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ("id", "user", "project", "permission", "role")
        read_only_fields = ("id",)
