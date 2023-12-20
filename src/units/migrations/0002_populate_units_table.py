from django.db import migrations


def add_units(apps, schema_editor):
    Unit = apps.get_model("units", "Unit")

    units = [
        {"name": "litre", "short_name": "L", "unit_type": "metric"},
        {"name": "decilitre", "short_name": "dL", "unit_type": "metric"},
        {"name": "centilitre", "short_name": "cL", "unit_type": "metric"},
        {"name": "millilitre", "short_name": "mL", "unit_type": "metric"},
        {"name": "kilogram", "short_name": "kg", "unit_type": "metric"},
        {"name": "gram", "short_name": "g", "unit_type": "metric"},
        {"name": "milligram", "short_name": "mg", "unit_type": "metric"},
        {"name": "teaspoon", "short_name": "tsp", "unit_type": "common"},
        {"name": "tablespoon", "short_name": "tbsp", "unit_type": "common"},
        {"name": "cup", "short_name": "c", "unit_type": "cup"},
        {"name": "ounce", "short_name": "oz", "unit_type": "imperial"},
        {"name": "pinch", "short_name": "pinch", "unit_type": "common"},
        {"name": "clove", "short_name": "clove", "unit_type": "common"},
        {"name": "head", "short_name": "head", "unit_type": "common"},
        {"name": "sheet", "short_name": "sheet", "unit_type": "common"},
        {"name": "piece", "short_name": "piece", "unit_type": "common"},
        {"name": "package", "short_name": "package", "unit_type": "common"},
    ]
    for unit in units:
        Unit.objects.create(**unit)


class Migration(migrations.Migration):
    dependencies = [
        ("units", "0001_initial"),
    ]

    operations = [migrations.RunPython(add_units, migrations.RunPython.noop)]
