import streamlit as st

st.title("SAT Math Coach 📘")
st.write("Welcome! This app will help you practice SAT Math with AI support.")

question = st.text_input("Enter a math problem:")
if question:
    st.write(f"🤔 You asked: {question}")
    st.write("👉 (Here we will later add AI-based solving using llm_client.py)")
