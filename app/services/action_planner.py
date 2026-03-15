from __future__ import annotations
from typing import Dict, List

EMOTION_TO_ACTIONS = {
    "joy": [
        "Celebrate the win",
        "Share gratitude with someone",
        "Journal what went well",
    ],
    "sadness": [
        "Reach out to a friend",
        "Take a short walk",
        "Write down one small next step",
    ],
    "anger": [
        "Pause for 10 deep breaths",
        "Identify the trigger and write it down",
        "Convert frustration into a concrete request",
    ],
    "fear": [
        "List what you can control",
        "Plan a small exposure step",
        "Talk to a supportive person",
    ],
    "disgust": [
        "Step away briefly",
        "Reflect on boundaries",
        "Reframe or seek a clean-up action",
    ],
    "anticipation": [
        "Outline the plan",
        "Schedule the next milestone",
        "Share expectations clearly",
    ],
    "trust": [
        "Acknowledge the partnership",
        "Document commitments",
        "Offer help proactively",
    ],
    "surprise": [
        "Pause and gather info",
        "Note new opportunities",
        "Adapt plan as needed",
    ],
    "neutral": [
        "Clarify your goal",
        "Decide the next action",
        "Timebox 15 minutes to start",
    ],
}


def plan_actions(emotion_scores: Dict[str, float]) -> List[str]:
    if not emotion_scores:
        return EMOTION_TO_ACTIONS["neutral"]

    # Choose the top emotion by score
    top_emotion = max(emotion_scores.items(), key=lambda kv: kv[1])[0]
    return EMOTION_TO_ACTIONS.get(top_emotion, EMOTION_TO_ACTIONS["neutral"])
