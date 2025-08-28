# chatbot.py
import requests
import json
import streamlit as st

def generate_response(user_input):
    messages = [{"role": msg["role"], "content": msg["content"]} for msg in st.session_state.get("conversation_history", [])]
    messages.append({"role": "user", "content": user_input})

    ai_content = ""
    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "mistral",
                "messages": messages
            },
            stream=True
        )
        response.raise_for_status()
        content_chunks = []
        for line in response.iter_lines():
            if line:
                try:
                    chunk = json.loads(line.decode("utf-8"))
                    if "message" in chunk and "content" in chunk["message"]:
                        content_chunks.append(chunk["message"]["content"])
                    elif "error" in chunk:
                        content_chunks.append(f"Ollama error: {chunk['error']}")
                except Exception:
                    continue
        ai_content = "".join(content_chunks) if content_chunks else "No valid response from Ollama."
    except Exception as e:
        ai_content = f"Error communicating with Ollama API: {e}"

    return ai_content
