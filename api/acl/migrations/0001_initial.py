# Generated by Django 5.1 on 2024-08-27 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Acl",
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
                ("service_account", models.TextField()),
                ("zone", models.TextField()),
            ],
            options={
                "verbose_name": "Access Control List",
                "verbose_name_plural": "Access Control Lists",
                "unique_together": {("service_account", "zone")},
            },
        ),
    ]
