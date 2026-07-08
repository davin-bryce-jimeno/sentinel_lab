import pytest
from rest_framework.test import APIClient

from events.models import LoginEvent

@pytest.fixture
def client():
    return APIClient()

@pytest.mark.django_db
def test_create_event(client):
    resp = client.post(
            "/api/events/",
            {"ip_address": "10.0.0.5", "username": "dj", "status": "FAILED"},
            format="json",
    )
    assert resp.status_code == 201
    assert LoginEvent.objects.count() == 1

@pytest.mark.django_db
def test_filter_by_status(client):
    LoginEvent.objects.create(ip_address="1.1.1.1", username="a", status="FAILED")
    LoginEvent.objects.create(ip_address="2.2.2.2", username="b", status="SUCCESS")

    resp = client.get("/api/events/?status=failed")

    assert resp.status_code == 200
    assert len(resp.json()) == 1
    assert resp.json()[0]["status"] == "FAILED"

@pytest.mark.django_db
def test_missing_field_is_rejected(client):
    resp = client.post(
            "/api/events/",
            {"ip_address": "10.0.0.5", "status": "FAILED"},
            format="json",
    )
    assert resp.status_code == 400
    assert "username" in resp.json()


