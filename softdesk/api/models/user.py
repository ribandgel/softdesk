from django.contrib.auth.models import AbstractUser
from django.db import models

from .constants import PERMISSION


class User(AbstractUser):
    class Meta:
        app_label = "api"


class Contributor(models.Model):
    from .project import Project

    user = models.ForeignKey(User, related_name="contributions", on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name="contributors", on_delete=models.CASCADE)
    permission = models.CharField(choices=PERMISSION, max_length=50)
    role = models.CharField(max_length=50)

    class Meta:
        app_label = "api"
