# Generated by Django 4.1.3 on 2023-10-05 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0004_profile"),
    ]

    operations = [
        migrations.DeleteModel(name="Profile",),
    ]