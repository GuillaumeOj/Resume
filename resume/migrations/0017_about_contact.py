# Generated by Django 3.0.7 on 2020-08-02 12:13

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("resume", "0016_auto_20200802_1407"),
    ]

    operations = [
        migrations.AddField(
            model_name="about",
            name="contact",
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
