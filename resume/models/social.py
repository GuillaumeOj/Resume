from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.core.validators import URLValidator
from django.db import models

from .about import About


class Social(models.Model):

    url = models.URLField(
        validators=[URLValidator, MinLengthValidator(5), MaxLengthValidator]
    )
    icon = models.CharField(
        max_length=50, validators=[MinLengthValidator(5), MaxLengthValidator]
    )

    title = models.CharField(
        max_length=100, validators=[MinLengthValidator(2), MaxLengthValidator]
    )

    about = models.ForeignKey(
        About, on_delete=models.CASCADE, related_name="related_about"
    )

    def __str__(self):
        return f"{self.title}"
