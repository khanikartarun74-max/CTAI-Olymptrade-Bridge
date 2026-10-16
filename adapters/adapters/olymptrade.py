
"""Olymptrade adapter scaffold for CTAI.

Live broker connectivity is intentionally not implemented yet.
This adapter never fabricates connection status, assets, or candles.
"""

from typing import Any

from adapters.base import BaseBrokerAdapter


class OlymptradeAdapter(BaseBrokerAdapter):
    """Isolated adapter interface for Olymptrade integration."""

    broker_name = "olymptrade"

    async def connect(self) -> bool:
        """Report unavailable until a supported connection is implemented."""
        self._connected = False
        self._last_error = "BROKER_CONNECTION_NOT_IMPLEMENTED"
        return False

    async def disconnect(self) -> None:
        """Reset local state; no live session is currently managed."""
        self._connected = False
        self._last_error = None

    async def get_assets(self) -> list[dict[str, Any]]:
        """No verified broker asset source is configured yet."""
        self._last_error = "ASSET_SOURCE_NOT_CONFIGURED"
        return []

    async def get_candles(
        self,
        symbol: str,
        timeframe: int,
        limit: int = 150,
    ) -> list[dict[str, Any]]:
        """Return no candles until live retrieval and validation exist."""
        if not symbol.strip():
            self._last_error = "SYMBOL_REQUIRED"
            return []

        if timeframe not in (60, 300, 900):
            self._last_error = "UNSUPPORTED_TIMEFRAME"
            return []

        if not 1 <= limit <= 150:
            self._last_error = "INVALID_CANDLE_LIMIT"
            return []

        self._last_error = "LIVE_CANDLE_SOURCE_NOT_CONFIGURED"
        return []
      
