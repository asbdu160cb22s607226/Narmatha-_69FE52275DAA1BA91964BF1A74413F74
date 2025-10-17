from emotion_to_action.actions import suggest_actions


def test_suggest_actions_default_count():
    suggestions = suggest_actions("joy")
    assert 1 <= len(suggestions) <= 3


def test_suggest_actions_max_limit():
    suggestions = suggest_actions("anger", max_suggestions=2)
    assert len(suggestions) == 2


def test_suggest_actions_unknown_emotion():
    suggestions = suggest_actions("unknown", max_suggestions=3)
    assert len(suggestions) == 3
