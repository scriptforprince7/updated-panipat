# Generated by Django 4.2.4 on 2023-08-29 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="best_deal",
            field=models.BooleanField(default=False),
        ),
    ]
