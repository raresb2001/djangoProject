# Generated by Django 4.2.3 on 2023-07-20 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trainer", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="trainer",
            name="profile",
            field=models.ImageField(null=True, upload_to="trainer_profiles/"),
        ),
    ]
