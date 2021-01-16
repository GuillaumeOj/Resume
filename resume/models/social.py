from django.core.validators import MinLengthValidator
from django.core.validators import URLValidator
from django.db import models


class Social(models.Model):

    url = models.URLField(validators=[URLValidator])
    title = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    icon = models.CharField(max_length=50, validators=[MinLengthValidator(5)])

    def __str__(self):
        return f"{self.title}"
