from __future__ import annotations
import sys
from typing import List

from .assistant import Assistant


def main(argv: List[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    if not argv:
        print("Usage: emotion-to-action \"your text here\"")
        return 2

    text = " ".join(argv)
    assistant = Assistant()
    result = assistant.analyze(text)

    if result.emotion is None:
        print("No emotion detected.")
        return 0

    print(f"Detected emotion: {result.emotion.name} (confidence={result.emotion.confidence:.2f})")
    if result.suggestions:
        print("Suggested actions:")
        for i, suggestion in enumerate(result.suggestions, start=1):
            print(f"  {i}. {suggestion}")
    else:
        print("No suggestions available.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
