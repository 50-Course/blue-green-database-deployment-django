# Generated by Django 5.0.2 on 2024-02-29 01:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mangapanels", "0001_initial"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                # it only change project state(blue), mark this ready for 'green' deployment
                migrations.AddField(
                    model_name="manga",
                    name="adapted",
                    field=models.BooleanField(blank=True, null=True),
                ),
            ],
            database_operations=[] # This is a no-op migration - meaning this is a migration that doesn't change anything in the database schema.    
        ),
    ]
