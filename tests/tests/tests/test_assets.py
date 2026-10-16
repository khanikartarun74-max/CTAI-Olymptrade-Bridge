
"""Asset registry and candle endpoint tests."""

from fastapi.testclient import TestClient

from bridge import app
from adapters.registry import available_brokers, get_adapter

client = TestClient(app)


def test_assets_endpoint_returns_empty_verified_registry() -> None:
    response = client.get("/api/assets")
    assert response.status_code == 200
    payload = response.json()
    assert payload["ok"] is True
    assert payload["broker"] == "olymptrade"
    assert payload["count"] == 0
    assert payload["assets"] == []


def test_candles_endpoint_reports_not_configured() -> None:
    response = client.get(
        "/api/market/candles",
        params={"symbol": "EURUSD", "timeframe": 60},
    )
    assert response.status_code == 503
    payload = response.json()
    assert payload["ok"] is False
    assert payload["error"] == "BROKER_CONNECTION_NOT_CONFIGURED"
    assert payload["candles"] == []


def test_invalid_timeframe_is_rejected() -> None:
    response = client.get(
        "/api/market/candles",
        params={"symbol": "EURUSD", "timeframe": 120},
    )
    assert response.status_code == 400


def test_registry_contains_only_olymptrade() -> None:
    assert available_brokers() == ["olymptrade"]
    adapter = get_adapter("olymptrade")
    assert adapter.broker_name == "olymptrade"
    assert adapter.connected is False
  
