from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional
import re


@dataclass(frozen=True)
class Emotion:
    name: str
    confidence: float


NEGATIVE_WORDS = {
    "sad": "sadness",
    "down": "sadness",
    "depressed": "sadness",
    "cry": "sadness",
    "angry": "anger",
    "mad": "anger",
    "furious": "anger",
    "rage": "anger",
    "scared": "fear",
    "afraid": "fear",
    "nervous": "fear",
    "anxious": "fear",
}

POSITIVE_WORDS = {
    "happy": "joy",
    "glad": "joy",
    "excited": "joy",
    "delighted": "joy",
    "love": "love",
    "grateful": "gratitude",
    "thankful": "gratitude",
}

NEUTRAL_WORDS = {
    "okay": "neutral",
    "fine": "neutral",
    "meh": "neutral",
}

WORD_TO_EMOTION = {**NEGATIVE_WORDS, **POSITIVE_WORDS, **NEUTRAL_WORDS}


def _tokenize(text: str) -> List[str]:
    return re.findall(r"[A-Za-z']+", text.lower())


def detect_emotion(text: str) -> Optional[Emotion]:
    tokens = _tokenize(text)
    if not tokens:
        return None

    score_by_emotion: dict[str, int] = {}
    for token in tokens:
        emotion = WORD_TO_EMOTION.get(token)
        if emotion is None:
            continue
        score_by_emotion[emotion] = score_by_emotion.get(emotion, 0) + 1

    if not score_by_emotion:
        # Heuristic: neutral when no cues present.
        return Emotion(name="neutral", confidence=0.5)

    # Choose the top emotion and normalize confidence by count share
    total = sum(score_by_emotion.values())
    top_emotion, top_count = max(score_by_emotion.items(), key=lambda kv: kv[1])
    confidence = top_count / total if total > 0 else 0.0
    return Emotion(name=top_emotion, confidence=confidence)
