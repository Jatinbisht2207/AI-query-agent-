from intent import detect_intent
from rag import load_vector_store, get_answer
from tools import mock_lead_capture
vectorstore = load_vector_store()


def format_response(query, context):
    q = query.lower()
    if "price" in q or "plan" in q:
        return f" Here are the pricing details:\n\n{context}"

    if "feature" in q or "benefit" in q:
        return f" Here are the key features:\n\n{context}"

    if "policy" in q:
        return f" Here’s the policy information:\n\n{context}"

    return f"Here’s what I found:\n\n{context}"


def handle_conversation(user_input, memory):
    if memory.stage == "ask_name":
        memory.name = user_input
        memory.stage = "ask_email"
        return "Great! Please enter your email."

    if memory.stage == "ask_email":
        if "@" not in user_input:
            return "Please enter a valid email address."
        memory.email = user_input
        memory.stage = "ask_platform"
        return "Which platform do you create content on? (YouTube/Instagram/etc.)"

    if memory.stage == "ask_platform":
        memory.platform = user_input

        if memory.is_complete():
            mock_lead_capture(memory.name, memory.email, memory.platform)
            memory.stage = None
            return " You're all set! Our team will contact you soon."

    intent = detect_intent(user_input)

    if intent == "GREETING":
        return "Hey! I'm AutoStream AI Assistant.\nI can help with pricing, features, or get you started 🚀"

    if intent == "HIGH_INTENT":
        memory.stage = "ask_name"
        return "Awesome! Let's get you started \nWhat's your name?"

    if intent == "PRODUCT_QUERY":
        context = get_answer(user_input, vectorstore)
        return format_response(user_input, context)

    if intent == "GENERAL":
        if len(user_input.split()) <= 1:
            return "Got it Let me know if you want pricing, features, or to get started "

        context = get_answer(user_input, vectorstore)
        return format_response(user_input, context)
    return "I'm not sure I understood. Can you rephrase?"