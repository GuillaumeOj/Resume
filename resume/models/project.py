from django.core.validators import MinLengthValidator
from django.db import models


class ProjectManager(models.Manager):
    def progression(self):
        projects = self.get_queryset().filter()

        if not projects:
            return 0

        achieved_projects = projects.filter(achieved=True)
        progression = len(achieved_projects) * 100 / len(projects)

        return progression


class Project(models.Model):

    name = models.CharField(max_length=100, validators=[MinLengthValidator(5)])

    number = models.IntegerField()

    achieved = models.BooleanField(default=False)
    pending = models.BooleanField(default=False)

    objects = ProjectManager()

    class Meta:
        ordering = ["number"]

    def __str__(self):
        return f"{self.name}"
