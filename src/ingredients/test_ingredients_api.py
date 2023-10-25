from django.urls import reverse
import pytest
from uuid import uuid4


@pytest.mark.django_db
def test_create_ingredient(client):
    url = reverse("api:ingredients")
    ingredient = {
        "name": "Ingredient test",
    }

    response = client.post(url, ingredient, content_type="application/json")

    assert response.status_code == 200
    assert response.json().get("id")


@pytest.mark.django_db
def test_create_invalid_ingredient(client):
    url = reverse("api:ingredients")
    ingredient = {
        "name": dict(wrong_type=True),
    }

    response = client.post(url, ingredient, content_type="application/json")

    assert response.status_code == 422


@pytest.mark.django_db
def test_create_invalid_ingredient_existing_id(client, simple_ingredient):
    url = reverse("api:ingredients")
    ingredient = {
        "id": simple_ingredient.id,
        "name": "Tomato",
    }
    response = client.post(url, ingredient, content_type="application/json")

    assert response.status_code == 409


@pytest.mark.django_db
def test_get_all_ingredients(client, simple_ingredient):
    url = reverse("api:ingredients")

    response = client.get(url)

    assert response.status_code == 200
    ingredients_list = response.json()
    assert isinstance(ingredients_list, list)
    assert ingredients_list, "List was empty, we expect at least one element"


@pytest.mark.django_db
def test_get_existing_ingredient(client, simple_ingredient):
    url = reverse("api:ingredients", kwargs=dict(ingredient_id=simple_ingredient.id))

    response = client.get(url)

    assert response.status_code == 200
    ingredient = response.json()
    assert ingredient.get("name") == simple_ingredient.name


@pytest.mark.django_db
def test_get_missing_ingredient(client):
    ingredient_id = uuid4()
    url = reverse("api:ingredients", kwargs=dict(ingredient_id=ingredient_id))

    response = client.get(url)

    assert response.status_code == 404


@pytest.mark.django_db
def test_update_ingredient(client, ingredient_to_update):
    url = reverse("api:ingredients", kwargs=dict(ingredient_id=ingredient_to_update.id))
    updated_ingredient = {
        "name": "Updated test ingredient",
    }

    response = client.put(url, updated_ingredient, content_type="application/json")

    assert response.status_code == 200
    assert response.json()["updated"]
    ingredient_to_update.refresh_from_db()
    assert ingredient_to_update.name == updated_ingredient.get("name")


@pytest.mark.django_db
def test_update_missing_ingredient(client):
    ingredient_id = uuid4()
    url = reverse("api:ingredients", kwargs=dict(ingredient_id=ingredient_id))
    updated_ingredient = {
        "name": "Updated test ingredient",
    }

    response = client.put(url, updated_ingredient, content_type="application/json")

    assert response.status_code == 404


@pytest.mark.django_db
def test_update_invalid_ingredient(client, ingredient_to_update):
    url = reverse("api:ingredients", kwargs=dict(ingredient_id=ingredient_to_update.id))
    updated_ingredient = {
        "all_ingredients": "Love",
    }

    response = client.put(url, updated_ingredient, content_type="application/json")

    assert response.status_code == 422
