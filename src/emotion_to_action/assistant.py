from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional

from .emotion import detect_emotion, Emotion
from .actions import suggest_actions


@dataclass
class AssistantResponse:
    text: str
    emotion: Optional[Emotion]
    suggestions: List[str]


class Assistant:
    def analyze(self, user_text: str, max_suggestions: int = 3) -> AssistantResponse:
        emotion = detect_emotion(user_text)
        if emotion is None:
            suggestions = []
            return AssistantResponse(text=user_text, emotion=None, suggestions=suggestions)

        suggestions = suggest_actions(emotion.name, max_suggestions=max_suggestions)
        return AssistantResponse(text=user_text, emotion=emotion, suggestions=suggestions)
