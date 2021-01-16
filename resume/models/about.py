from django.core.validators import MinLengthValidator
from django.db import models


class About(models.Model):

    first_name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    place = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    contact = models.EmailField()
    country = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    description = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
