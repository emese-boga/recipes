import pytest

from django.contrib.admin.sites import AdminSite
from django.urls import reverse

from .admin import UnitAdmin
from .models import Unit


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


@pytest.mark.django_db
def test_unit_admin_site_has_delete_permission():
    site = AdminSite()
    unit_admin = UnitAdmin(Unit, site)
    assert not unit_admin.has_delete_permission(None)


@pytest.mark.django_db
def test_unit_admin_site_has_add_permission():
    site = AdminSite()
    unit_admin = UnitAdmin(Unit, site)
    assert not unit_admin.has_add_permission(None)


@pytest.mark.django_db
def test_unit_admin_site_has_change_permission():
    site = AdminSite()
    unit_admin = UnitAdmin(Unit, site)
    assert not unit_admin.has_change_permission(None)
