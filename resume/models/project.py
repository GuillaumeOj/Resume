from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.db import models

from .about import About


class ProjectManager(models.Manager):
    def progression(self, about):
        """Return the progression in percent.
        :return: a value in percent of the progression
        """

        projects = self.get_queryset().filter(about=about)

        progression = 0.0

        if projects:
            achieved_projects = projects.filter(achieved=True)
            progression = len(achieved_projects) * 100 / len(projects)

        return progression


class Project(models.Model):

    name = models.CharField(
        max_length=100, validators=[MinLengthValidator(5), MaxLengthValidator]
    )

    number = models.IntegerField()

    achieved = models.BooleanField(default=False)
    pending = models.BooleanField(default=False)

    about = models.ForeignKey(About, on_delete=models.CASCADE, default=1)

    objects = ProjectManager()

    class Meta:
        ordering = ["number"]

    def __str__(self):
        return f"{self.name}"
