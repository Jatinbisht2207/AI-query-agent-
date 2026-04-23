def detect_intent(user_input):
    text = user_input.lower().strip()
    words = text.split()

    if any(word in words for word in ["hi", "hello", "hey"]):
        return "GREETING"
    
    if text in ["pro plan", "premium plan", "start plan"]:
        return "HIGH_INTENT"

    if any(word in words for word in [
        "price", "pricing", "cost", "plan", "feature", "features", "policy"
    ]):
        return "PRODUCT_QUERY"

    high_intent_phrases = [
        "try pro plan",
        "start pro plan",
        "buy",
        "subscribe",
        "sign up",
        "get started"
    ]

    if any(phrase in text for phrase in high_intent_phrases):
        return "HIGH_INTENT"

    return "GENERAL"