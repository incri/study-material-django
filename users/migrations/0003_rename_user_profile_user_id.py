# Generated by Django 4.2 on 2023-05-07 11:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_remove_profile_user_id_profile_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="user",
            new_name="user_id",
        ),
    ]
