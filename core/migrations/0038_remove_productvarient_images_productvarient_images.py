# Generated by Django 4.2.4 on 2023-10-15 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0037_productvarient"),
    ]

    operations = [
        migrations.RemoveField(model_name="productvarient", name="images",),
        migrations.AddField(
            model_name="productvarient",
            name="images",
            field=models.ManyToManyField(blank=True, to="core.productimages"),
        ),
    ]
