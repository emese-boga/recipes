import re

from rest_framework import serializers

from .models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=80, allow_blank=True)

    class Meta:
        model = Ingredient
        fields = ["id", "name"]

    def validate_name(self, value):
        ingredient = Ingredient.objects.filter(name=value)
        if ingredient:
            raise serializers.ValidationError("Ingredient name already exists")

        pattern = r"^[a-zA-Z0-9()\-\'\" ]*$"

        if not re.match(pattern, value):
            raise serializers.ValidationError("The name contains illegal characters")

        return value
