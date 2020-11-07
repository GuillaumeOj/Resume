from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.db import models

from .pathway import PathWay


class About(models.Model):

    first_name = models.CharField(
        max_length=100, validators=[MinLengthValidator(2), MaxLengthValidator]
    )

    last_name = models.CharField(
        max_length=100, validators=[MinLengthValidator(2), MaxLengthValidator]
    )

    place = models.CharField(
        max_length=100, validators=[MinLengthValidator(2), MaxLengthValidator]
    )

    contact = models.EmailField()

    country = models.CharField(
        max_length=100, validators=[MinLengthValidator(2), MaxLengthValidator]
    )

    description = models.TextField()

    paths = models.ManyToManyField(PathWay)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
