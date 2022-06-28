# Generated by Django 4.0.3 on 2022-03-10 17:56

import django.utils.timezone
from django.db import migrations, models

import temba.utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="APIToken",
            fields=[
                ("is_active", models.BooleanField(default=True)),
                ("key", models.CharField(max_length=40, primary_key=True, serialize=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Resthook",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "is_active",
                    models.BooleanField(
                        default=True, help_text="Whether this item is active, use this instead of deleting"
                    ),
                ),
                (
                    "created_on",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="When this item was originally created",
                    ),
                ),
                (
                    "modified_on",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="When this item was last modified",
                    ),
                ),
                ("slug", models.SlugField(help_text="A simple label for this event")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ResthookSubscriber",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "is_active",
                    models.BooleanField(
                        default=True, help_text="Whether this item is active, use this instead of deleting"
                    ),
                ),
                (
                    "created_on",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="When this item was originally created",
                    ),
                ),
                (
                    "modified_on",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="When this item was last modified",
                    ),
                ),
                ("target_url", models.URLField(help_text="The URL that we will call when our ruleset is reached")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="WebHookEvent",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("data", temba.utils.models.JSONAsTextField(default=dict)),
                ("action", models.CharField(default="POST", max_length=8)),
                ("created_on", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
