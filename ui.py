# ui.py
import streamlit as st

def display_messages(conversation_history):
    for msg in conversation_history:
        if msg["role"] == "user":
            st.markdown(f'<div class="user-message">{msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="ai-message">{msg["content"]}</div>', unsafe_allow_html=True)


def input_box():
    return st.text_input("How can I help you today?")

def action_buttons():
    col1, col2 = st.columns(2)
    pos_affirmation = col1.button("Give me a positive affirmation")
    guided_meditation = col2.button("Give me a guided meditation")
    return pos_affirmation, guided_meditation

def display_text(text, label):
    st.markdown(f"**{label}:** {text}")

def show_spinner(message):
    return st.spinner(message)
