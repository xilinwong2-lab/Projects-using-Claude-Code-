from typing import List


def find_similar_items(category: str, style: str, color: str, user) -> List[dict]:
    """
    Placeholder for shopping API integration (e.g. ASOS, Shopify).
    Returns mock results so the endpoint is functional before a real API is wired in.
    """
    return [
        {
            "name": f"{color.title()} {category.title()} — Style Match",
            "brand": "Coming soon",
            "price": None,
            "url": None,
            "image_url": None,
            "note": "Connect a shopping API (ASOS, Shopify) to populate real results.",
        }
    ]
