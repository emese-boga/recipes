from django.urls import reverse
import pytest
from uuid import uuid4


@pytest.mark.django_db
def test_create_recipe_valid_data(client):
    url = reverse("recipes_list_create")
    recipe = {
        "name": "Recipe testing",
        "description": "Recipe for testing",
        "instructions": "Run tests to complete recipe",
    }

    response = client.post(url, recipe, content_type="application/json")

    assert response.status_code == 201
    data = response.json()
    assert data
    assert data.get("data")


@pytest.mark.django_db
def test_create_recipe_invalid_name_field_type(client):
    url = reverse("recipes_list_create")
    recipe = {
        "name": list({1, 2, 3}),
        "description": "Recipe for testing",
        "instructions": "Run tests to complete recipe",
    }

    response = client.post(url, recipe, content_type="application/json")

    assert response.status_code == 400


@pytest.mark.django_db
def test_create_recipe_missing_mandatory_field(client):
    url = reverse("recipes_list_create")
    recipe = {
        "name": "Recipe testing",
        "description": "Recipe for testing",
    }

    response = client.post(url, recipe, content_type="application/json")

    assert response.status_code == 400


@pytest.mark.django_db
def test_create_invalid_recipe_with_existing_name_fails(client, simple_recipe):
    url = reverse("recipes_list_create")
    recipe = {
        "name": f"{simple_recipe.name}",
        "description": "Recipe for testing",
        "instructions": "Run tests to complete recipe",
    }

    response = client.post(url, recipe, content_type="application/json")

    assert response.status_code == 400
    errors = response.json()
    assert errors
    assert errors.get("error")


@pytest.mark.django_db
def test_get_all_recipes(client, simple_recipe):
    url = reverse("recipes_list_create")

    response = client.get(url)

    assert response.status_code == 200
    recipes_list = response.json()
    assert recipes_list
    assert recipes_list.get("data")
    assert isinstance(recipes_list.get("data"), list)


@pytest.mark.django_db
def test_get_existing_recipe(client, simple_recipe):
    url = reverse("recipes", kwargs=dict(id=simple_recipe.id))

    response = client.get(url)

    assert response.status_code == 200
    recipe = response.json()
    assert recipe
    assert recipe.get("data")
    assert recipe.get("data").get("name") == simple_recipe.name


@pytest.mark.django_db
def test_get_missing_recipe(client):
    recipe_id = uuid4()
    url = reverse("recipes", kwargs=dict(id=recipe_id))

    response = client.get(url)

    assert response.status_code == 404


@pytest.mark.django_db
def test_update_recipe_valid_data(client, recipe_to_update):
    url = reverse("recipes", kwargs=dict(id=str(recipe_to_update.id)))
    updated_recipe = {"description": "Updated description"}

    response = client.put(url, updated_recipe, content_type="application/json")

    assert response.status_code == 200
    recipe_to_update.refresh_from_db()
    assert recipe_to_update.description == updated_recipe.get("description")


@pytest.mark.django_db
def test_update_missing_recipe(client):
    recipe_id = str(uuid4())
    url = reverse("recipes", kwargs=dict(id=recipe_id))
    updated_recipe = {"name": "Updated test recipe"}

    response = client.put(url, updated_recipe, content_type="application/json")

    assert response.status_code == 404


@pytest.mark.django_db
def test_update_recipe_with_invalid_name_fails(client, recipe_to_update):
    url = reverse("recipes", kwargs=dict(id=str(recipe_to_update.id)))
    updated_recipe = {"name": "????????????"}

    response = client.put(url, updated_recipe, content_type="application/json")

    assert response.status_code == 400
    errors = response.json()
    assert errors
    assert errors.get("error")


@pytest.mark.django_db
def test_delete_operation_not_supported(client, recipe_to_update):
    url = reverse("recipes", kwargs=dict(id=str(recipe_to_update.id)))

    response = client.delete(url, content_type="application/json")

    assert response.status_code == 405
