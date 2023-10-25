import pytest
from recipes import models as recipe_models
from ingredients import models as ingredient_models


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


@pytest.fixture
def simple_ingredient():
    ingredient = ingredient_models.Ingredient.objects.create(
        name="Test ingredient",
    )
    return ingredient


@pytest.fixture
def ingredient_to_update():
    ingredient = ingredient_models.Ingredient.objects.create(
        name="Test ingredient for update",
    )
    return ingredient
