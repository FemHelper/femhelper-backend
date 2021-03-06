# Generated by Django 2.2 on 2020-02-09 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_remove_user_device_id"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Chat",
            new_name="Messages",
        ),
        migrations.CreateModel(
            name="Requests",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("date_time_creation", models.DateTimeField(auto_now_add=True)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_id",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ChatRoom",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("last_message_time", models.DateTimeField()),
                ("date_time_creation", models.DateTimeField(auto_now_add=True)),
                (
                    "participant1_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="participant1_id",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "participant2_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="participant2_id",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
