import json
import os

BASE_PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_PATH, "data", "glitch_knowledge_base.json")


def load_data():
    with open(DATA_PATH, "r") as f:
        return json.load(f)


def calculate_confidence(matches, text_len):
    if text_len < 10:
        return 0.25

    if matches == 0:
        return 0.30

    score = 0.45 + (matches * 0.15)
    return round(min(score, 0.95), 2)


def guardrail(conf):
    if conf >= 0.8:
        return "High confidence, but still verify in your game engine."
    elif conf >= 0.5:
        return "Medium confidence. More detail would improve accuracy."
    else:
        return "Low confidence. Human review recommended."


def analyze_glitch(text):
    if not text or len(text.strip()) < 5:
        return {
            "glitch_type": "unclear",
            "confidence": 0.1,
            "likely_causes": ["Input too short."],
            "suggested_fixes": ["Add more details about the glitch."],
            "guardrail": "Insufficient input."
        }

    data = load_data()
    text = text.lower()

    best = None
    best_matches = 0

    for item in data:
        matches = sum(1 for kw in item["keywords"] if kw in text)

        if matches > best_matches:
            best_matches = matches
            best = item

    if best is None:
        return {
            "glitch_type": "unknown",
            "confidence": 0.3,
            "likely_causes": ["No strong match found."],
            "suggested_fixes": [
                "Check logs",
                "Reproduce the issue",
                "Inspect recent code changes"
            ],
            "guardrail": "Unknown issue. Needs manual debugging."
        }

    conf = calculate_confidence(best_matches, len(text))

    return {
        "glitch_type": best["type"],
        "confidence": conf,
        "likely_causes": best["causes"],
        "suggested_fixes": best["fixes"],
        "guardrail": guardrail(conf)
    }
