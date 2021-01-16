from django.core.validators import MinLengthValidator
from django.db import models


PRO = "PRO"
EDU = "EDU"
EXPERIENCES_TYPES = [(PRO, "Profesionnal"), (EDU, "Education")]


class Experience(models.Model):

    title = models.CharField(max_length=100, validators=[MinLengthValidator(5)])
    subtitle = models.CharField(max_length=100, validators=[MinLengthValidator(5)])

    description = models.TextField(blank=True)

    start = models.DateField()
    end = models.DateField()

    experience_type = models.CharField(
        max_length=3, choices=EXPERIENCES_TYPES, default=PRO
    )

    class Meta:
        ordering = ["-end"]

    def __str__(self):
        return f"{self.title}"
