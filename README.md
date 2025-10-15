# Emotion to Action Smart Assistant (Flask)

A minimal Flask backend that analyzes text for emotions and suggests actions.

## Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python wsgi.py
```

Health check:
```bash
curl -s http://localhost:8000/health
```

Analyze text:
```bash
curl -s -X POST http://localhost:8000/api/analyze \
  -H 'Content-Type: application/json' \
  -d '{"text":"I am stressed and a bit angry"}' | jq
```

## Notes
- Uses NRCLex if available; falls back to simple heuristics without it.
- Maps dominant emotion to a small set of suggested next actions.
