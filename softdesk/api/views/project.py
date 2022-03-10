from django.db.models import Q
from rest_framework.permissions import IsAuthenticated

from softdesk.api.models import Comment, Issue, Project
from softdesk.api.serializers import CommentSerializer, IssueSerializer, ProjectSerializer

from .common import AtomicModelViewSet


class ProjectViewSet(AtomicModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer

    def get_queryset(self):
        if self.request and not self.request.user.is_anonymous:
            queryset = Project.objects.filter(author=self.request.user)
        else:
            queryset = Project.objects.none()
        return queryset.order_by("-id")


class IssueViewSet(AtomicModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = IssueSerializer

    def get_queryset(self):
        if self.request and not self.request.user.is_anonymous:
            queryset = Issue.objects.filter(
                Q(author=self.request.user) | Q(assignee=self.request.user)
            )
        else:
            queryset = Issue.objects.none()
        return queryset.order_by("-id")


class CommentViewSet(AtomicModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        if self.request and not self.request.user.is_anonymous:
            queryset = Comment.objects.filter(author=self.request.user)
        else:
            queryset = Comment.objects.none()
        return queryset.order_by("-id")
