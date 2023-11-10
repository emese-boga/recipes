# Generated by Django 4.2.5 on 2023-11-10 12:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("ingredients", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ingredient",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="ingredient",
            name="name",
            field=models.CharField(max_length=80, unique=True),
        ),
    ]
