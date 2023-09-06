from django.urls import reverse_lazy


def test_healthcheck(client):
    url = reverse_lazy("api:healthcheck")
    response = client.get(url)
    assert response.status_code == 200
    assert response.json()["success"]
