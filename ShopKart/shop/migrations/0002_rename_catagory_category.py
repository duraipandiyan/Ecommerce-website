# Generated by Django 4.1.3 on 2023-08-19 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="catagory", new_name="category",),
    ]