# Generated by Django 3.1.1 on 2020-10-11 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("resume", "0020_project_pending"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="project",
            options={"ordering": ["number"]},
        ),
    ]
