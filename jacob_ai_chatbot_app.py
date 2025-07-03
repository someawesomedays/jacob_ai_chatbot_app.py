import streamlit as st
from datetime import datetime
import random

# --- Personal Info ---
name = "Jacob Isaacson"
birthday = "1972-01-07"
weight = 187
zodiac_sign = "Capricorn"
image_url = "https://i.imgur.com/NlWVX2e.jpg"

capricorn_traits = ["Disciplined", "Responsible", "Ambitious", "Practical", "Patient", "Determined"]
lucky_numbers = [3, 7, 21, 28, 33, 44]
quotes = [
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Discipline is the bridge between goals and accomplishment.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Your time is limited, don’t waste it living someone else’s life.",
    "The best way to predict the future is to create it."
]

# --- Age ---
def calculate_age(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    today = datetime.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

age = calculate_age(birthday)

# --- Simulated AI Response (Placeholder for OpenAI/GPT API) ---
def ai_response(user_input):
    user_input = user_input.lower()

    if "name" in user_input:
        return f"My name is {name}."
    elif "age" in user_input:
        return f"I’m {age} years old."
    elif "birthday" in user_input:
        return f"My birthday is {birthday}."
    elif "zodiac" in user_input or "sign" in user_input:
        return f"I’m a proud {zodiac_sign} ♑!"
    elif "trait" in user_input:
        return f"My Capricorn traits are: {', '.join(capricorn_traits)}."
    elif "lucky" in user_input:
        return f"My lucky numbers are {', '.join(map(str, lucky_numbers))}."
    elif "quote" in user_input:
        return random.choice(quotes)
    elif "weight" in user_input:
        return f"I weigh {weight} pounds."
    elif "picture" in user_input:
        return "Here's my picture:"
    else:
        return "I'm still learning, but try asking me about my zodiac, age, birthday, or a quote."

# --- UI ---
st.set_page_config(page_title="Jacob Isaacson AI Chatbot", page_icon="🧠", layout="centered")
tab1, tab2 = st.tabs(["🤖 ChatBot", "👤 Profile"])

# --- TAB 1: ChatBot ---
with tab1:
    st.header("Chat with Jacob")
    st.image(image_url, width=150)

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Use text_input which supports voice typing on mobile
    user_input = st.text_input("Ask me anything:", "")

    if user_input:
        response = ai_response(user_input)
        st.session_state.chat_history.append(("🧑 You", user_input))
        st.session_state.chat_history.append(("🤖 Bot", response))

    for sender, msg in st.session_state.chat_history:
        if msg == "Here's my picture:":
            st.markdown(f"**{sender}:** {msg}")
            st.image(image_url, width=200)
        else:
            st.markdown(f"**{sender}:** {msg}")

# --- TAB 2: Profile View ---
with tab2:
    st.header("Jacob Isaacson's Profile")
    st.image(image_url, width=200, caption="Jacob Isaacson")

    st.subheader("📌 Basic Info")
    st.write(f"**Birthday:** {birthday}")
    st.write(f"**Age:** {age}")
    st.write(f"**Weight:** {weight} lbs")
    st.write(f"**Zodiac Sign:** {zodiac_sign} ♑")

    st.subheader("🧠 Personality Traits")
    st.write(", ".join(capricorn_traits))

    st.subheader("🍀 Lucky Numbers")
    st.write(", ".join(str(n) for n in lucky_numbers))

    st.subheader("💬 Inspirational Quote")
    st.info(random.choice(quotes))

    st.caption("Built with ❤️ by Jacob Isaacson using Streamlit on Android")
