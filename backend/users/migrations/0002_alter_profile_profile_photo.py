# Generated by Django 5.0.6 on 2024-06-12 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_photo",
            field=models.ImageField(
                default="default.jpg", upload_to="media/users_profile_images"
            ),
        ),
    ]
