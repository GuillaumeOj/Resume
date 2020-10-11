from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.db import models


class PathWay(models.Model):

    title = models.CharField(
        max_length=100, validators=[MinLengthValidator(5), MaxLengthValidator]
    )

    def __str__(self):
        return f"{self.title}"
