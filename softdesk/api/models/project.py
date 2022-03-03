from django.contrib.auth import get_user_model
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    author = models.ForeignKey(get_user_model(), related_name="projects", on_delete=models.CASCADE)

    class Meta:
        app_label = "api"


class Issue(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)
    project = models.ForeignKey(Project, related_name="issues", on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    author = models.ForeignKey(get_user_model(), related_name="issues", on_delete=models.CASCADE)
    assignee = models.ForeignKey(
        get_user_model(), related_name="assignments", on_delete=models.SET_NULL, null=True
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "api"


class Comment(models.Model):
    description = models.CharField(max_length=50)
    author = models.ForeignKey(get_user_model(), related_name="comments", on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, related_name="comments", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "api"
