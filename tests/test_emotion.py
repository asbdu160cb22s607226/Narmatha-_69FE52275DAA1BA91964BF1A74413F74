from emotion_to_action.emotion import detect_emotion


def test_detect_emotion_positive():
    e = detect_emotion("I am so happy and excited today!")
    assert e is not None
    assert e.name in {"joy"}
    assert 0.0 < e.confidence <= 1.0


def test_detect_emotion_negative():
    e = detect_emotion("I'm sad and a bit depressed.")
    assert e is not None
    assert e.name == "sadness"


def test_detect_emotion_neutral_fallback():
    e = detect_emotion("Just writing some text with no obvious cues.")
    assert e is not None
    assert e.name == "neutral"
