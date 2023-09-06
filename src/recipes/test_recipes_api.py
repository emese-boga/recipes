from django.urls import reverse
import pytest
from uuid import uuid4


@pytest.mark.django_db
def test_create_recipe(client):
    url = reverse("api:recipes")
    recipe = {
        "name": "Recipe testing",
        "description": "Recipe for testing",
        "instructions": "Run tests to complete recipe",
    }

    response = client.post(url, recipe, content_type="application/json")

    assert response.status_code == 200
    assert response.json().get("id")


@pytest.mark.django_db
def test_create_invalid_recipe(client):
    url = reverse("api:recipes")
    recipe = {
        "name": list({1, 2, 3}),
        "description": "Recipe for testing",
        "instructions": "Run tests to complete recipe",
    }

    response = client.post(url, recipe, content_type="application/json")

    assert response.status_code == 422


@pytest.mark.django_db
def test_create_invalid_recipe_existing_id(client, simple_recipe):
    url = reverse("api:recipes")
    recipe = {
        "id": simple_recipe.id,
        "name": "Test name",
        "description": "Recipe for testing",
        "instructions": "Run tests to complete recipe",
    }

    response = client.post(url, recipe, content_type="application/json")

    assert response.status_code == 409


@pytest.mark.django_db
def test_get_all_recipes(client, simple_recipe):
    url = reverse("api:recipes")

    response = client.get(url)

    assert response.status_code == 200
    recipes_list = response.json()
    assert isinstance(recipes_list, list)
    assert recipes_list, "List was empty, we expect at least one element"


@pytest.mark.django_db
def test_get_existing_recipe(client, simple_recipe):
    url = reverse("api:recipes", kwargs=dict(recipe_id=simple_recipe.id))

    response = client.get(url)

    assert response.status_code == 200
    recipe = response.json()
    assert recipe.get("name") == simple_recipe.name


@pytest.mark.django_db
def test_get_missing_recipe(client):
    recipe_id = uuid4()
    url = reverse("api:recipes", kwargs=dict(recipe_id=recipe_id))

    response = client.get(url)

    assert response.status_code == 404


@pytest.mark.django_db
def test_update_recipe(client, recipe_to_update):
    url = reverse("api:recipes", kwargs=dict(recipe_id=recipe_to_update.id))
    updated_recipe = {
        "name": "Updated test recipe",
        "description": "Updated description",
        "instructions": "Updated instructions",
    }

    response = client.put(url, updated_recipe, content_type="application/json")

    assert response.status_code == 200
    assert response.json()["updated"]
    recipe_to_update.refresh_from_db()
    assert recipe_to_update.name == updated_recipe.get("name")


@pytest.mark.django_db
def test_update_missing_recipe(client):
    recipe_id = uuid4()
    url = reverse("api:recipes", kwargs=dict(recipe_id=recipe_id))
    updated_recipe = {
        "name": "Updated test recipe",
        "description": "Updated description",
        "instructions": "Updated instructions",
    }

    response = client.put(url, updated_recipe, content_type="application/json")

    assert response.status_code == 404


@pytest.mark.django_db
def test_update_invalid_recipe(client, recipe_to_update):
    url = reverse("api:recipes", kwargs=dict(recipe_id=recipe_to_update.id))
    updated_recipe = {
        "all_ingredients": "Patience",
        "description": "Updated description",
        "instructions": "Updated instructions",
    }

    response = client.put(url, updated_recipe, content_type="application/json")

    assert response.status_code == 422
