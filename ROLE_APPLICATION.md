# TechTrio AI & Automation Intern — Portfolio Note

## Why this repo is relevant
APIShield-AI is a small FastAPI automation service that turns API telemetry into a structured, explainable action decision. It demonstrates the parts of AI/automation work I can contribute immediately: Python, REST APIs, data validation, deterministic scoring, backend integration and testable decision logic.

## What I built
- FastAPI inspection endpoint
- Per-client behavioral event windows
- Burst, error-ratio, path-scanning and latency signals
- Weighted risk score with human-readable reasons
- Allow / challenge / block policy output
- Unit test for an abusive traffic pattern

## What I would build next for TechTrio
1. Replace demo input with an authorized business webhook/API source.
2. Add n8n workflow triggers around safe, allowlisted actions.
3. Persist audit events in SQLite/Postgres.
4. Add retries, idempotency and exception queues.
5. Package with Docker and simple deployment documentation.

## Integrity
This is a defensive portfolio project using synthetic telemetry. It is not a live client system and does not perform offensive scanning.