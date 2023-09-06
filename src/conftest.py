import pytest
from recipes import models as recipe_models


@pytest.fixture
def simple_recipe():
    recipe = recipe_models.Recipe.objects.create(
        name="Test recipe",
        description="A simple recipe for testing",
        instructions="Create this recipe by running some tests",
    )
    return recipe


@pytest.fixture
def recipe_to_update():
    recipe = recipe_models.Recipe.objects.create(
        name="Test recipe for update",
        description="A simple recipe for testing",
        instructions="Create this recipe by running some tests",
    )
    return recipe
