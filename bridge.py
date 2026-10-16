
import os
import logging
from datetime import datetime, timezone
from typing import Any

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

APP_NAME = "CTAI-Olymptrade-Bridge"
APP_VERSION = "0.1.0"

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO").upper(),
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(APP_NAME)

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description=(
        "Separate Olymptrade bridge foundation. "
        "Live broker connectivity is not configured yet."
    ),
)


class StatusResponse(BaseModel):
    ok: bool
    service: str
    version: str
    connected: bool
    market_data_ready: bool
    message: str


@app.get("/")
def root() -> dict[str, Any]:
    return {
        "service": APP_NAME,
        "version": APP_VERSION,
        "message": "Backend is running. Broker integration is not configured.",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health() -> dict[str, Any]:
    return {
        "ok": True,
        "service": APP_NAME,
        "version": APP_VERSION,
        "server_time": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/api/status", response_model=StatusResponse)
def api_status() -> StatusResponse:
    # Do not claim a live connection until a real adapter is implemented
    # and its connection state has been verified.
    return StatusResponse(
        ok=True,
        service=APP_NAME,
        version=APP_VERSION,
        connected=False,
        market_data_ready=False,
        message="Olymptrade adapter is not connected or verified.",
    )


@app.get("/api/assets")
def get_assets() -> dict[str, Any]:
    # Empty registry is intentional: do not invent supported assets.
    return {
        "ok": True,
        "broker": "olymptrade",
        "count": 0,
        "assets": [],
        "message": "Asset registry has not been populated from a verified source.",
    }


@app.get("/api/market/candles")
def get_candles(
    symbol: str,
    timeframe: int = 60,
) -> JSONResponse:
    if not symbol.strip():
        return JSONResponse(
            status_code=400,
            content={"ok": False, "error": "symbol is required"},
        )

    if timeframe not in (60, 300, 900):
        return JSONResponse(
            status_code=400,
            content={
                "ok": False,
                "error": "timeframe must be 60, 300, or 900 seconds",
            },
        )

    # Live candle retrieval is deliberately unavailable until the
    # official/supported broker connection has been implemented.
    return JSONResponse(
        status_code=503,
        content={
            "ok": False,
            "broker": "olymptrade",
            "symbol": symbol,
            "timeframe": timeframe,
            "candles": [],
            "error": "BROKER_CONNECTION_NOT_CONFIGURED",
            "message": "No live candle data is available yet.",
        },
    )


@app.on_event("startup")
async def startup_event() -> None:
    logger.info("%s starting; broker connection is not configured", APP_NAME)


@app.on_event("shutdown")
async def shutdown_event() -> None:
    logger.info("%s shutting down", APP_NAME)
  
