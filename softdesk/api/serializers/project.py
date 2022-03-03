from rest_framework import serializers

from softdesk.api.models import Comment, Issue, Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "title", "description", "type", "author")
        read_only_fields = ("id",)


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = (
            "id",
            "title",
            "description",
            "tag",
            "priority",
            "project",
            "status",
            "author",
            "assignee",
            "created",
        )
        read_only_fields = ("id",)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "description", "author", "issue", "created")
        read_only_fields = ("id",)
