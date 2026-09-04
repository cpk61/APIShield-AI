# APIShield-AI

Adaptive API abuse and anomaly detector with per-client behavioral windows, burst detection and interpretable risk scoring.

## Features
- FastAPI inspection endpoint
- Sliding per-client event window
- Burst, error-ratio, path-scanning and latency risk signals
- Explainable reasons and allow/challenge/block actions
- No external API keys
- Unit test for abusive traffic pattern

## Run
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Test
```bash
pytest -q
```

## Architecture
`API Event -> Client Window -> Risk Signals -> Weighted Risk -> Policy Action + Reasons`

## Important
This is a defensive security portfolio project. It scores application telemetry and does not perform offensive scanning or exploitation.
