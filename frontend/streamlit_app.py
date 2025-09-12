import streamlit as st
import pandas as pd
from llm_client import LLMClient  # your custom wrapper

# Load sample problems
data = pd.read_csv("data/sample_problems.csv")

# Initialize LLM client
llm = LLMClient()

st.title("SAT Math Coach")

st.write("Welcome! Ask me any SAT Math question.")

# User input
question = st.text_input("Enter your math question:")

if st.button("Get Solution"):
    if question:
        answer = llm.get_answer(question)  # Your LLM call
        st.write(f"**Answer:** {answer}")
    else:
        st.write("Please enter a question.")
        
# Optionally display sample problems
if st.checkbox("Show sample problems"):
    st.dataframe(data.head(10))
