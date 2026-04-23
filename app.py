import streamlit as st
from main import handle_conversation
from memory import Memory
import time

st.set_page_config(page_title="AutoStream AI", layout="centered")


st.markdown("""
<style>

/* App background */
.stApp {
    background-color: #0b1220;
}

/* Chat container */
.chat-container {
    max-width: 700px;
    margin: auto;
}

/* USER bubble */
.user-bubble {
    background-color: #1e293b;
    color: #ffffff;
    padding: 10px 15px;
    border-radius: 12px;
    display: inline-block;
    max-width: 70%;
    font-size: 15px;
}

/* BOT bubble */
.bot-bubble {
    background-color: #e2e8f0;
    color: #111827 !important;
    padding: 10px 15px;
    border-radius: 12px;
    display: inline-block;
    max-width: 70%;
    font-size: 15px;
}

/* Fix nested text */
.bot-bubble * {
    color: #111827 !important;
}

/* Chat alignment */
.chat-row {
    display: flex;
    align-items: flex-end;
    margin: 10px 0;
}

.right {
    justify-content: flex-end;
}

.left {
    justify-content: flex-start;
}

/* Avatar circles */
.avatar {
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background-color: #334155;
    display: inline-block;
    margin: 0 8px;
}

/* Input styling */
textarea {
    border-radius: 20px !important;
}

</style>
""", unsafe_allow_html=True)

st.title("AutoStream AI Assistant")

# Initialize memory
if "memory" not in st.session_state:
    st.session_state.memory = Memory()

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f"""
            <div class="chat-row right">
                <div class="user-bubble">
                    {msg["content"]}
                </div>
                <div class="avatar"></div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div class="chat-row left">
                <div class="avatar"></div>
                <div class="bot-bubble">
                    {msg["content"].replace("\\n", "<br>")}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# Input box
user_input = st.chat_input("Type a message...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Typing indicator (clean)
    typing_placeholder = st.empty()
    typing_placeholder.markdown(
        "<div style='color:#94a3b8; font-size:14px;'>Typing...</div>",
        unsafe_allow_html=True
    )

    time.sleep(0.6)

    # Get response
    response = handle_conversation(user_input, st.session_state.memory)

    typing_placeholder.empty()

    # Add bot message
    st.session_state.messages.append({"role": "bot", "content": response})

    st.rerun()