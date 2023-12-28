import streamlit as st
from openai import OpenAI
import os

# Postavljanje API ključa
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Ovde menjate naslov i podnaslov Chatbot aplikacije
st.title("💬 AI Chatbot")
st.caption("Vaš lični asistent za AI i inovacije powerd by ChatGPT 🚀✨")

# Postavljanje inicijalne poruke u session_state
if "messages" not in st.session_state:
  st.session_state["messages"] = [{
      "role":
      "assistant",
      "content":
      "Ti si moj lični asistent specijalizovan za veštačku inteligenciju i inovacije. Svaki odgovor ćeš slati na srpskom jeziku."  # Prompt za programiranje ChatGPT-a
  }]

# Prikazivanje poruka osim prve inicijalne
for msg in st.session_state.messages[1:]:
  st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
  st.session_state.messages.append({"role": "user", "content": prompt})
  st.chat_message("user").write(prompt)

  with st.spinner("🤔 Razmišljam..."):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=st.session_state.messages)  # ChatGPT model
    msg = response.choices[0].message.content

  st.session_state.messages.append({"role": "assistant", "content": msg})
  st.chat_message("assistant").write(msg)
