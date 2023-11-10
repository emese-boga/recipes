import re

from rest_framework import serializers

from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=80, allow_blank=True)
    description = serializers.CharField(max_length=256, allow_blank=True)
    instructions = serializers.CharField(allow_blank=True)

    class Meta:
        model = Recipe
        fields = ["id", "name", "created", "description", "instructions"]

    def validate_name(self, value):
        recipe = Recipe.objects.filter(name=value)
        if recipe:
            raise serializers.ValidationError("Recipe name already exists")

        pattern = r"^[a-zA-Z0-9_.,:()\-\'\" ]*$"

        if not re.match(pattern, value):
            raise serializers.ValidationError("The name contains illegal characters")

        return value
