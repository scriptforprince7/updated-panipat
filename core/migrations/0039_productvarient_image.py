# Generated by Django 4.2.4 on 2023-10-15 07:05

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0038_remove_productvarient_images_productvarient_images"),
    ]

    operations = [
        migrations.AddField(
            model_name="productvarient",
            name="image",
            field=models.ImageField(
                default="productvarient.jpg", upload_to=core.models.user_directory_path
            ),
        ),
    ]
