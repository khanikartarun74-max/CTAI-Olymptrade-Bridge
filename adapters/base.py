
"""Common interface for CTAI broker adapters."""

from abc import ABC, abstractmethod
from typing import Any


class BaseBrokerAdapter(ABC):
    """Base interface for broker-specific integrations."""

    broker_name: str = "unknown"

    def __init__(self) -> None:
        self._connected = False
        self._last_error: str | None = None

    @property
    def connected(self) -> bool:
        """Return the adapter's verified connection state."""
        return self._connected

    @property
    def last_error(self) -> str | None:
        """Return the most recent connection or data error."""
        return self._last_error

    def status(self) -> dict[str, Any]:
        """Return a safe status snapshot."""
        return {
            "broker": self.broker_name,
            "connected": self._connected,
            "last_error": self._last_error,
        }

    @abstractmethod
    async def connect(self) -> bool:
        """Connect to the broker using a supported method."""
        raise NotImplementedError

    @abstractmethod
    async def disconnect(self) -> None:
        """Close the broker connection and release resources."""
        raise NotImplementedError

    @abstractmethod
    async def get_assets(self) -> list[dict[str, Any]]:
        """Return assets verified from the broker data source."""
        raise NotImplementedError

    @abstractmethod
    async def get_candles(
        self,
        symbol: str,
        timeframe: int,
        limit: int = 150,
    ) -> list[dict[str, Any]]:
        """Return validated candles from the real broker source."""
        raise NotImplementedError
      
