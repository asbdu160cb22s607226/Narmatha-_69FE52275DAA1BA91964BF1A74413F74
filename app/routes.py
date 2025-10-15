from flask import Blueprint, jsonify, request
from .services.text_emotion import analyze_text_emotion
from .services.action_planner import plan_actions

bp = Blueprint("api", __name__)


@bp.post("/analyze")
def analyze():
    payload = request.get_json(silent=True) or {}
    text = (payload.get("text") or "").strip()
    if not text:
        return jsonify({"error": "Field 'text' is required"}), 400

    analysis = analyze_text_emotion(text)
    actions = plan_actions(analysis)

    return jsonify({
        "input": text,
        "analysis": analysis,
        "actions": actions,
    })
