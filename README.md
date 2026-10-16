
# CTAI-Olymptrade-Bridge

A dedicated backend bridge for the CTAI trading platform's
future Olymptrade integration.

## Current Status

- Backend foundation: In progress
- Health endpoint: Implemented
- API status endpoint: Implemented
- Asset registry: Not connected to a verified broker source
- Live candle data: Not configured
- Olymptrade session connection: Not implemented
- Production deployment: Not verified

This service must not report a live broker connection until a real,
supported connection has been implemented and verified.

## Features

- FastAPI backend
- Health and status endpoints
- Explicit unavailable responses for unconfigured market data
- Environment-based configuration
- Automated API tests
- Separate service from other CTAI broker bridges

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Service information |
| GET | `/health` | Backend health check |
| GET | `/api/status` | Broker connection status |
| GET | `/api/assets` | Asset registry |
| GET | `/api/market/candles` | Candle API interface |
| GET | `/docs` | Interactive API documentation |

### Candle Request

Example:

`/api/market/candles?symbol=EURUSD&timeframe=60`

Supported timeframe values in the current API scaffold:

- `60` seconds
- `300` seconds
- `900` seconds

The candle endpoint currently returns an unavailable response
because live broker data retrieval has not been implemented.

## Requirements

- Python 3.11 or a compatible supported Python version
- pip
- Packages listed in `requirements.txt`

## Local Setup

Create and activate a Python virtual environment, then install
the dependencies:

```bash
python -m venv .venv
```

On Linux or macOS:

```bash
source .venv/bin/activate
```

Install packages:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn bridge:app --host 0.0.0.0 --port 8000
```

Open the interactive documentation at:

`http://127.0.0.1:8000/docs`

## Configuration

Use `.env.example` as a template for configuration.

Never commit real session identifiers, passwords, access tokens,
or other broker credentials to GitHub.

No real Olymptrade credentials are required for the current
backend scaffold.

## Testing

Run:

```bash
pytest
```

Tests should verify the health endpoint, status response,
asset registry response, and unavailable candle behavior.

## Deployment

The intended deployment target is a separate Render web service.

Suggested start command:

```bash
uvicorn bridge:app --host 0.0.0.0 --port $PORT
```

Deploy only after the required files and automated tests
have been checked.

## Security and Data Integrity

- Do not expose broker credentials in frontend code.
- Do not invent assets, prices, candles, or connection status.
- Keep this bridge separate from the Pocket Option bridge.
- Add a real broker adapter only after its connection method
  and data format have been verified.
- Add authentication and rate limiting before exposing
  sensitive endpoints publicly.

## Roadmap

1. Complete the backend foundation.
2. Add and test the adapter interface.
3. Verify a supported Olymptrade connection method.
4. Implement real asset discovery and candle retrieval.
5. Add connection recovery and data validation.
6. Run automated tests before deployment.
7. Connect the bridge to CTAI after verification.

## Disclaimer

This repository is a software integration project.
It does not guarantee trading accuracy, profitability,
or uninterrupted broker connectivity.
