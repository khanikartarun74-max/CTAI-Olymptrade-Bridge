
"""Registry for CTAI broker adapters."""

from typing import Any

from adapters.base import BaseBrokerAdapter
from adapters.olymptrade import OlymptradeAdapter


_ADAPTER_FACTORIES: dict[str, type[BaseBrokerAdapter]] = {
    "olymptrade": OlymptradeAdapter,
}


def available_brokers() -> list[str]:
    """Return broker adapters registered in this service."""
    return sorted(_ADAPTER_FACTORIES.keys())


def get_adapter(broker_name: str) -> BaseBrokerAdapter:
    """Create an adapter for a registered broker."""
    normalized_name = broker_name.strip().lower()

    if not normalized_name:
        raise ValueError("broker_name is required")

    factory = _ADAPTER_FACTORIES.get(normalized_name)

    if factory is None:
        raise ValueError(
            f"Unsupported broker: {normalized_name}"
        )

    return factory()


def adapter_statuses() -> list[dict[str, Any]]:
    """Return safe status snapshots for registered adapters."""
    statuses: list[dict[str, Any]] = []

    for broker_name in available_brokers():
        adapter = get_adapter(broker_name)
        statuses.append(adapter.status())

    return statuses
  
