# Generated by Django 4.2.11 on 2024-05-07 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_rename_contry_myuser_city_rename_sity_myuser_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="marketplace",
            name="marketplace_name",
            field=models.CharField(default="", max_length=64),
        ),
    ]
