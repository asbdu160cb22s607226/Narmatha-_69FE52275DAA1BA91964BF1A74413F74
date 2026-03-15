from __future__ import annotations
from typing import List, Dict


SUGGESTIONS: Dict[str, List[str]] = {
    "sadness": [
        "Take a short walk and get fresh air",
        "Write down three things you're grateful for",
        "Call a friend or loved one",
        "Listen to a calming playlist",
    ],
    "anger": [
        "Pause and take ten deep breaths",
        "Journal what triggered you and why",
        "Take a break; step away for five minutes",
        "Do a quick workout to release tension",
    ],
    "fear": [
        "Name the fear and rate it 1-10",
        "Try a 4-7-8 breathing pattern",
        "Break the problem into one tiny step",
        "Ask someone you trust for support",
    ],
    "joy": [
        "Celebrate the win with someone",
        "Capture this moment in a journal",
        "Share your positive energy with a kind message",
        "Plan a small reward for yourself",
    ],
    "gratitude": [
        "Send a note to thank someone",
        "Start a gratitude list for the week",
        "Do an act of kindness today",
        "Reflect on why you feel grateful",
    ],
    "love": [
        "Express it with a thoughtful message",
        "Spend quality time with someone you care about",
        "Do a small act of service",
        "Savor the feeling for a few breaths",
    ],
    "neutral": [
        "Set a tiny goal for the next hour",
        "Take a mindful break and stretch",
        "Hydrate and check in with your body",
        "Organize your workspace for 5 minutes",
    ],
}


DEFAULT_FALLBACK = [
    "Take a deep breath",
    "Drink a glass of water",
    "Do a two-minute stretch",
]


def suggest_actions(emotion_name: str, max_suggestions: int = 3) -> List[str]:
    if max_suggestions <= 0:
        return []

    suggestions = SUGGESTIONS.get(emotion_name.lower(), DEFAULT_FALLBACK)
    return suggestions[:max_suggestions]
