# Generated by Django 4.0.3 on 2022-03-10 17:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("orgs", "0093_squashed"),
        ("archives", "0015_squashed"),
    ]

    operations = [
        migrations.AddField(
            model_name="archive",
            name="org",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="archives", to="orgs.org"
            ),
        ),
        migrations.AddField(
            model_name="archive",
            name="rollup",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to="archives.archive"),
        ),
        migrations.AlterUniqueTogether(
            name="archive",
            unique_together={("org", "archive_type", "start_date", "period")},
        ),
    ]
