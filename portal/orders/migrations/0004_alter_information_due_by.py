# Generated by Django 4.2.11 on 2024-05-08 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0003_alter_order_worker_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="information", name="due_by", field=models.SmallIntegerField(),
        ),
    ]
