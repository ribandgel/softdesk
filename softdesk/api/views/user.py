from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from softdesk.api.models import Contributor, User
from softdesk.api.serializers import ContributorSerializer, UserSerializer
from .common import AtomicModelViewSet


class UserViewSet(GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request and not self.request.user.is_anonymous:
            queryset = User.objects.get(id=self.request.user.id)
        else:
            queryset = User.objects.none()
        return queryset.order_by("-id")


class ContributorViewSet(AtomicModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ContributorSerializer

    def get_queryset(self):
        if self.request and not self.request.user.is_anonymous:
            queryset = Contributor.objects.filter(user=self.request.user)
        else:
            queryset = Contributor.objects.none()
        return queryset.order_by("-id")
