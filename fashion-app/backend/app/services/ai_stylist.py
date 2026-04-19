import json
from typing import List, Optional
import anthropic

from app.config import settings

client = anthropic.Anthropic(api_key=settings.anthropic_api_key)


def suggest_outfits(wardrobe, user, occasion: Optional[str], destination: Optional[str]) -> List[dict]:
    wardrobe_summary = [
        {
            "id": item.id,
            "name": item.name,
            "category": item.category,
            "color": item.color,
            "style_tags": json.loads(item.style_tags) if item.style_tags else [],
        }
        for item in wardrobe
    ]

    prompt = f"""You are a personal AI stylist. Given this user's wardrobe and profile, suggest 3 outfit combinations.

User profile:
- Body shape: {user.body_shape or "unknown"}
- Skin tone: {user.skin_tone or "unknown"}
- Style preferences: {user.style_preferences or "not set"}
- Celebrity inspirations: {user.celebrity_inspirations or "none"}

Occasion: {occasion or "everyday"}
Destination/context: {destination or "not specified"}

Wardrobe (JSON):
{json.dumps(wardrobe_summary, indent=2)}

Respond ONLY with a valid JSON array of outfit objects. Each object must have:
- "name": short outfit name
- "item_ids": list of clothing item IDs from the wardrobe
- "notes": one sentence styling tip

Example:
[{{"name": "Casual Sunday", "item_ids": [1, 3], "notes": "Roll up the sleeves for a relaxed look."}}]
"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = message.content[0].text.strip()
    return json.loads(raw)
