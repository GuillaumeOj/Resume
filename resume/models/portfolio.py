from django.core.validators import MinLengthValidator
from django.db import models
import django.utils


class PortfolioCategory(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Portfolio(models.Model):
    title = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    subtitle = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    description = models.TextField()
    link = models.URLField()

    publishing_date = models.DateField(default=django.utils.timezone.now)

    portfolio_categories = models.ManyToManyField(PortfolioCategory)

    class Meta:
        ordering = ["-publishing_date"]

    def __str__(self):
        return f"{self.title}"
