# Generated by Django 3.0.7 on 2020-08-02 11:45

import django.core.validators
from django.db import migrations
from django.db import models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("resume", "0011_auto_20200802_1331"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        validators=[
                            django.core.validators.MinLengthValidator(5),
                            django.core.validators.MaxLengthValidator,
                        ],
                    ),
                ),
                ("achieve", models.BooleanField(default=False)),
                (
                    "about",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="resume.About"
                    ),
                ),
            ],
        ),
    ]
