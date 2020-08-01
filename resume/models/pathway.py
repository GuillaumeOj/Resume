from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


class PathWay(models.Model):

    title = models.CharField(
        max_length=100, validators=[MinLengthValidator(5), MaxLengthValidator]
    )

    def __str__(self):
        return f"<PathWay: {self.title}>"
