from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.db import models

from .about import About


class Project(models.Model):

    name = models.CharField(
        max_length=100, validators=[MinLengthValidator(5), MaxLengthValidator]
    )

    number = models.IntegerField()

    achieved = models.BooleanField(default=False)
    about = models.ForeignKey(About, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.name}"
