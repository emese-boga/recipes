from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_retrieve_units(client):
    url = reverse("get_units")

    response = client.get(url)

    assert response.status_code == 200
    data = response.json()
    assert data
    assert data.get("data")


@pytest.mark.django_db
def test_not_supported_request_type(client):
    url = reverse("get_units")

    response = client.post(url)

    assert response.status_code == 405
