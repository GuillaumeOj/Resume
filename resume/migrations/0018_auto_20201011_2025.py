# Generated by Django 3.1.1 on 2020-10-11 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("resume", "0017_about_contact"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="experience",
            options={"ordering": ["end"]},
        ),
    ]
