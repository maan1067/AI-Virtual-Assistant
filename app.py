import streamlit as st
import webbrowser
import time
from datetime import datetime
from assistant import ask_ollama

st.set_page_config(
    page_title="AI Virtual Assistant",
    page_icon="🤖",
    layout="wide"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:

    st.title("🤖 AI Assistant")

    st.divider()

    st.write("### 👨‍💻 Developer")
    st.write("Maan Ebrahim")

    st.write("### 🏢 Internship")
    st.write("Hex Softwares")

    st.write("### 🧠 Model")
    st.write("Llama 3.2")

    st.write("### 📊 Status")
    st.success("Online")

    st.write("### 💬 Messages")

    message_count = len(st.session_state.messages)

    st.metric("Total Messages", message_count)

    st.divider()

    st.info("Local AI Assistant powered by Ollama")

st.title("🤖 AI Virtual Assistant")

if len(st.session_state.messages) == 0:

    st.info("""
# 👋 Welcome!

### I'm your AI Virtual Assistant.

You can ask me about:

- 💻 Programming
- 🤖 Artificial Intelligence
- 📚 General Knowledge
- 🧮 Mathematics
- 🌐 Technology

Type your question below to start chatting.
""")

st.write("Powered by Ollama (Llama 3.2)")

col1, col2 = st.columns([5, 1])

with col2:
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Type your message...")

if question:

    with st.chat_message("user"):
        st.markdown(question)

    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    command = question.lower().strip()

    if command == "open google":
        webbrowser.open("https://www.google.com")
        answer = "🌐 Opening Google..."

    elif command == "open youtube":
        webbrowser.open("https://www.youtube.com")
        answer = "🎬 Opening YouTube..."

    elif command == "open github":
        webbrowser.open("https://github.com")
        answer = "💻 Opening GitHub..."

    elif command == "what time is it":
        answer = f"🕒 {datetime.now().strftime('%H:%M:%S')}"

    elif command == "what is today's date":
        answer = f"📅 {datetime.now().strftime('%d-%m-%Y')}"

    else:
        with st.spinner("🤖 AI is thinking..."):
            answer = ask_ollama(question)

    with st.chat_message("assistant"):

        placeholder = st.empty()

        full_text = ""

        st.markdown(answer)

        placeholder.markdown(full_text)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )