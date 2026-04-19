import base64
import json
import anthropic

from app.config import settings

client = anthropic.Anthropic(api_key=settings.anthropic_api_key)


def classify_image(image_bytes: bytes) -> dict:
    """Send clothing image to Claude Vision and extract category, color, and style tags."""
    b64 = base64.standard_b64encode(image_bytes).decode("utf-8")

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=256,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {"type": "base64", "media_type": "image/jpeg", "data": b64},
                    },
                    {
                        "type": "text",
                        "text": (
                            "Analyse this clothing item image. Respond ONLY with valid JSON containing:\n"
                            '- "name": short descriptive name (e.g. "White linen shirt")\n'
                            '- "category": one of [top, bottom, dress, skirt, outerwear, accessory, shoes]\n'
                            '- "color": dominant color\n'
                            '- "style_tags": list of up to 3 style keywords (e.g. ["casual", "summer"])\n'
                        ),
                    },
                ],
            }
        ],
    )

    raw = message.content[0].text.strip()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"category": "other", "color": None, "style_tags": []}
