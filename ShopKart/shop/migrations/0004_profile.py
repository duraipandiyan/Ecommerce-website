# Generated by Django 4.1.3 on 2023-10-03 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_rename_category_product_categorys"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        default="profile_pics/default.jpg", upload_to="profile_pics/"
                    ),
                ),
            ],
        ),
    ]
