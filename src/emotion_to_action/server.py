from __future__ import annotations
from fastapi import FastAPI
from pydantic import BaseModel, Field

from .assistant import Assistant


app = FastAPI(title="Emotion to Action Assistant", version="0.1.0")
assistant = Assistant()


class AnalyzeRequest(BaseModel):
    text: str = Field(..., min_length=1)
    max_suggestions: int = Field(3, ge=0, le=10)


class AnalyzeResponse(BaseModel):
    text: str
    emotion: str | None
    confidence: float | None
    suggestions: list[str]


@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze(req: AnalyzeRequest) -> AnalyzeResponse:
    result = assistant.analyze(req.text, max_suggestions=req.max_suggestions)
    if result.emotion is None:
        return AnalyzeResponse(text=req.text, emotion=None, confidence=None, suggestions=[])

    return AnalyzeResponse(
        text=result.text,
        emotion=result.emotion.name,
        confidence=result.emotion.confidence,
        suggestions=result.suggestions,
    )


def run() -> None:
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
