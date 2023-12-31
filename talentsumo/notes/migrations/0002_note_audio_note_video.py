# Generated by Django 4.2 on 2023-06-21 17:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("notes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="note",
            name="audio",
            field=models.FileField(blank=True, upload_to="notes/audio/"),
        ),
        migrations.AddField(
            model_name="note",
            name="video",
            field=models.FileField(blank=True, upload_to="notes/video/"),
        ),
    ]
