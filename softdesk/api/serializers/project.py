from rest_framework import serializers

from softdesk.api.models import Comment, Issue, Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "title", "description", "type", "author")
        read_only_fields = ("id", "author")

    def create(self, validated_data):
        author = self.context["request"].user
        return Project.objects.create(author=author, **validated_data)


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
        read_only_fields = ("id", "author")

    def create(self, validated_data):
        author = self.context["request"].user
        return Issue.objects.create(author=author, **validated_data)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "description", "author", "issue", "created")
        read_only_fields = ("id", "author")

    def create(self, validated_data):
        author = self.context["request"].user
        return Comment.objects.create(author=author, **validated_data)
