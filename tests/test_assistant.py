from emotion_to_action.assistant import Assistant


def test_assistant_analyze():
    assistant = Assistant()
    res = assistant.analyze("Feeling nervous and a bit afraid about tomorrow", max_suggestions=2)
    assert res.emotion is not None
    assert res.emotion.name == "fear"
    assert len(res.suggestions) == 2
