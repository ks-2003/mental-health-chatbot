# app.py
import streamlit as st
import chatbot
import ui

st.set_page_config(page_title="Mental Health Support Agent")
st.title("Mental Health Support Agent")

if "conversation_history" not in st.session_state:
    st.session_state["conversation_history"] = []

# Display conversation
ui.display_messages(st.session_state["conversation_history"])

user_input = ui.input_box()

if user_input:
    with ui.show_spinner("Thinking..."):
        response = chatbot.generate_response(user_input)
        st.session_state["conversation_history"].append({"role": "user", "content": user_input})
        st.session_state["conversation_history"].append({"role": "assistant", "content": response})
    st.rerun()

pos_affirmation_clicked, guided_meditation_clicked = ui.action_buttons()

if pos_affirmation_clicked:
    with ui.show_spinner("Generating positive affirmation..."):
        response = chatbot.generate_response("Provide a positive affirmation to someone who is stressed.")
        st.session_state["conversation_history"].append({"role": "assistant", "content": response})
    st.rerun()

if guided_meditation_clicked:
    with ui.show_spinner("Generating guided meditation..."):
        response = chatbot.generate_response("Provide a 5-minute guided meditation for relaxation.")
        st.session_state["conversation_history"].append({"role": "assistant", "content": response})
    st.rerun()
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

