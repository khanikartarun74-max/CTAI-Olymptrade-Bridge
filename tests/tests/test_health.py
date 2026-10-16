
"""Health and status endpoint tests."""

from fastapi.testclient import TestClient

from bridge import app

client = TestClient(app)


def test_root_endpoint() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["service"] == "CTAI-Olymptrade-Bridge"


def test_health_endpoint() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    payload = response.json()
    assert payload["ok"] is True
    assert payload["service"] == "CTAI-Olymptrade-Bridge"


def test_status_does_not_claim_broker_connection() -> None:
    response = client.get("/api/status")
    assert response.status_code == 200
    payload = response.json()
    assert payload["connected"] is False
    assert payload["market_data_ready"] is False
  
