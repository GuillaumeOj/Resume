from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

from .pathway import PathWay
from .about import About


class Experience(models.Model):

    title = models.CharField(
        max_length=100, validators=[MinLengthValidator(5), MaxLengthValidator]
    )

    subtitle = models.CharField(
        max_length=100, validators=[MinLengthValidator(5), MaxLengthValidator]
    )

    description = models.TextField(blank=True)

    start = models.DateField()

    end = models.DateField()

    path = models.ForeignKey(PathWay, on_delete=models.CASCADE)
    about = models.ForeignKey(About, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
