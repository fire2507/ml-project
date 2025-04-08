import streamlit as st

st.set_page_config(page_title="Mental Health Chatbot", page_icon="💬")

st.title("💬 Mental Health Support Chatbot")
st.write("I'm here for you. Talk to me anytime 💙")

user_input = st.text_input("How are you feeling today?")

responses = {
    "sad": "I'm really sorry you're feeling this way. It's okay to feel sad sometimes. Want to try a 5-minute breathing exercise?",
    "anxious": "Anxiety can be overwhelming. Let's try grounding yourself: name 3 things you can see, 2 you can touch, 1 you can hear.",
    "stressed": "Stress is tough. Consider taking a short break or writing down what's overwhelming you.",
    "happy": "That's amazing to hear! Remember this moment and what made you smile 💫",
    "lonely": "You are not alone. Reaching out like this is a strong first step. I'm always here to listen."
}

if user_input:
    response = "I'm here to support you. Could you tell me more?"  # default
    for keyword in responses:
        if keyword in user_input.lower():
            response = responses[keyword]
            break
    st.write(f"🤖: {response}")
