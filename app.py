import streamlit as st
import random
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 AI Chatbot Assistant")
if "messages" not in st.session_state:
    st.session_state.messages = []
responses = {
    "hello": [
        "Hey there 😄",
        "Hello 👋",
        "Hi! How can I help you?"
    ],
    "how are you": [
        "I am doing great 😄",
        "Awesome as always 🔥",
        "Feeling intelligent today 🤖"
    ],
    "what is your name": [
        "I am your AI Chatbot 🤖",
        "You can call me Bhargav Bot 😄"
    ],
    "bye": [
        "Goodbye 👋",
        "See you again 😄",
        "Take care 🔥"
    ],
    "thank you": [
        "You're welcome 😄",
        "Happy to help 👍",
        "Anytime bro 🔥"
    ],
    "who created you": [
        "Bhargav created me 😎🔥"
    ]
}
user_input = st.text_input("💬 Enter your message")
if st.button("Send"):
    st.session_state.messages.append(
        ("You", user_input)
    )
    reply = responses.get(
        user_input.lower(),
        ["Sorry bro 😅 I don't understand that yet."]
    )
    bot_reply = random.choice(reply)
    st.session_state.messages.append(
        ("Bot", bot_reply)
    )
st.subheader("📜 Chat History")
for sender, message in st.session_state.messages:
    if sender == "You":
        st.markdown(
            f"🧑 **You:** {message}"
        )
    else:
        st.markdown(
            f"🤖 **Bot:** {message}"
        )
