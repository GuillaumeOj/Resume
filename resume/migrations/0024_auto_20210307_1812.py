# Generated by Django 3.1.7 on 2021-03-07 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0023_portfolio_portfoliocategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='categories',
            new_name='portfolio_categories',
        ),
    ]
