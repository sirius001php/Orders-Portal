# Generated by Django 4.2.11 on 2024-06-19 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0015_alter_sourseassets_size_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sourseassets",
            name="size_file",
            field=models.IntegerField(default=10),
        ),
    ]