from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, URLValidator


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

    def __str__(self):
        return f"<Social link: {self.title}>"
