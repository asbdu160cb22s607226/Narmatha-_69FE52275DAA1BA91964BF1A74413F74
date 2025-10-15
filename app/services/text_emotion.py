from __future__ import annotations
from typing import Dict

try:
    from nrclex import NRCLex
except Exception:  # pragma: no cover - allows running without lib during init
    NRCLex = None  # type: ignore


def analyze_text_emotion(text: str) -> Dict[str, float]:
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not text.strip():
        return {"neutral": 1.0}

    if NRCLex is None:
        # Fallback simple heuristic if NRCLex is unavailable
        lowered = text.lower()
        if any(word in lowered for word in ["happy", "joy", "glad", "delight"]):
            return {"joy": 1.0}
        if any(word in lowered for word in ["sad", "down", "unhappy", "depressed"]):
            return {"sadness": 1.0}
        if any(word in lowered for word in ["angry", "mad", "furious", "rage"]):
            return {"anger": 1.0}
        if any(word in lowered for word in ["scared", "afraid", "fear", "terrified"]):
            return {"fear": 1.0}
        return {"neutral": 1.0}

    # Real analysis using NRCLex
    doc = NRCLex(text)
    raw = doc.raw_emotion_scores  # e.g., {'joy': 3, 'sadness': 1}
    total = sum(raw.values()) or 1
    normalized = {k: v / total for k, v in raw.items()}

    # If nothing recognized, call it neutral
    if not normalized:
        return {"neutral": 1.0}

    return normalized
