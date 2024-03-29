# Generated by Django 4.1.5 on 2023-02-14 16:53

from django.db import migrations, models
import django.db.models.deletion
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("resource_tracker", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SpecialDie",
            fields=[
                (
                    "id",
                    model_utils.fields.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "game_template",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="special_dice",
                        to="resource_tracker.gametemplate",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SpecialDieFace",
            fields=[
                (
                    "id",
                    model_utils.fields.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("count", models.PositiveIntegerField(default=1)),
                (
                    "die",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="faces",
                        to="resource_tracker.specialdie",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
