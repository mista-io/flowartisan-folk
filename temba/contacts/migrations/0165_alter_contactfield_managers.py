# Generated by Django 4.0.3 on 2022-04-20 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0164_remove_contactfield_field_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactfield",
            name="org",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="fields", to="orgs.org"),
        ),
        migrations.AlterModelManagers(
            name="contactfield",
            managers=[],
        ),
    ]
