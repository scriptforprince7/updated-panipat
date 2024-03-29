# Generated by Django 4.2.4 on 2023-12-13 10:20

from django.db import migrations
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0070_remove_productvarient_meta_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='bottom_page_description',
            field=django_summernote.fields.SummernoteTextField(max_length=35000),
        ),
        migrations.AlterField(
            model_name='sub_categories',
            name='bottom_page_description',
            field=django_summernote.fields.SummernoteTextField(max_length=35000),
        ),
    ]
