from django.urls import reverse
import pytest
from uuid import uuid4


@pytest.mark.django_db
def test_create_ingredient(client):
    url = reverse("ingredients_list_create")
    ingredient = {
        "name": "Ingredient test",
    }

    response = client.post(url, ingredient, content_type="application/json")

    assert response.status_code == 201
    data = response.json()
    assert data
    assert data.get("data")


@pytest.mark.django_db
def test_create_ingredient_with_invalid_name_field_type(client):
    url = reverse("ingredients_list_create")
    ingredient = {
        "name": dict(wrong_type=True),
    }

    response = client.post(url, ingredient, content_type="application/json")

    assert response.status_code == 400


@pytest.mark.django_db
def test_create_invalid_ingredient_with_existing_name(client, simple_ingredient):
    url = reverse("ingredients_list_create")
    ingredient = {
        "name": simple_ingredient.name,
    }

    response = client.post(url, ingredient, content_type="application/json")

    assert response.status_code == 400
    errors = response.json()
    assert errors
    assert errors.get("error")


@pytest.mark.django_db
def test_get_all_ingredients(client, simple_ingredient):
    url = reverse("ingredients_list_create")

    response = client.get(url)

    assert response.status_code == 200
    ingredients_list = response.json()
    assert ingredients_list
    assert ingredients_list.get("data")
    assert isinstance(ingredients_list.get("data"), list)


@pytest.mark.django_db
def test_get_existing_ingredient(client, simple_ingredient):
    url = reverse("ingredients", kwargs=dict(id=simple_ingredient.id))

    response = client.get(url)

    assert response.status_code == 200
    ingredient = response.json()
    assert ingredient
    ingredient_data = ingredient.get("data")
    assert ingredient_data
    assert ingredient_data.get("name") == simple_ingredient.name


@pytest.mark.django_db
def test_get_missing_ingredient(client):
    id = uuid4()
    url = reverse("ingredients", kwargs=dict(id=id))

    response = client.get(url)

    assert response.status_code == 404


@pytest.mark.django_db
def test_update_ingredient(client, ingredient_to_update):
    url = reverse("ingredients", kwargs=dict(id=ingredient_to_update.id))
    updated_ingredient = {
        "name": "Updated test ingredient",
    }

    response = client.put(url, updated_ingredient, content_type="application/json")

    assert response.status_code == 200
    ingredient_to_update.refresh_from_db()
    assert ingredient_to_update.name == updated_ingredient.get("name")


@pytest.mark.django_db
def test_update_missing_ingredient(client):
    id = uuid4()
    url = reverse("ingredients", kwargs=dict(id=id))
    updated_ingredient = {
        "name": "Updated test ingredient",
    }

    response = client.put(url, updated_ingredient, content_type="application/json")

    assert response.status_code == 404


@pytest.mark.django_db
def test_update_ingredient_with_invalid_name(client, ingredient_to_update):
    url = reverse("ingredients", kwargs=dict(id=ingredient_to_update.id))
    updated_ingredient = {
        "name": "???????????????",
    }

    response = client.put(url, updated_ingredient, content_type="application/json")

    assert response.status_code == 400
    errors = response.json()
    assert errors
    assert errors.get("error")


@pytest.mark.django_db
def test_delete_operation_not_supported(client, ingredient_to_update):
    url = reverse("ingredients", kwargs=dict(id=str(ingredient_to_update.id)))

    response = client.delete(url, content_type="application/json")

    assert response.status_code == 405
