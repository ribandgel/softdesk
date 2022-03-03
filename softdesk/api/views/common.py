from django.db import transaction
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


def lock_for_update(func):
    def _lock_for_update(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        if self.action in ["update", "partial_update", "destroy"] + list(
            getattr(self, "extra_lock_for_update", [])
        ):
            result = result.select_for_update(of=getattr(self, "lock_for_update_of", ("self",)))
        return result

    return _lock_for_update


class AtomicCreateModelMixin(mixins.CreateModelMixin):
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class AtomicUpdateModelMixin(mixins.UpdateModelMixin):
    @transaction.atomic
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class AtomicDestroyModelMixin(mixins.DestroyModelMixin):
    @transaction.atomic
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class AtomicModelViewSetMixin(
    AtomicUpdateModelMixin, AtomicCreateModelMixin, AtomicDestroyModelMixin
):
    pass


class AtomicModelViewSet(
    AtomicCreateModelMixin,
    mixins.RetrieveModelMixin,
    AtomicUpdateModelMixin,
    AtomicDestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    pass
