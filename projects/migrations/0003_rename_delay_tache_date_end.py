# Generated by Django 4.2.9 on 2024-01-25 04:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_rename_delais_tache_delay_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tache",
            old_name="delay",
            new_name="date_end",
        ),
    ]
