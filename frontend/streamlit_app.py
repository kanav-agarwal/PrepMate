# frontend/streamlit_app.py
import streamlit as st
import requests
import json

BACKEND = "http://localhost:8000"

st.title("CoachK — SAT Math Tutor (Demo)")

q = st.text_area("Enter SAT-style math question", height=100)
student_ans = st.text_input("Your answer (optional)")

if st.button("Ask Tutor"):
    payload = {"question": q, "student_answer": student_ans}
    res = requests.post(BACKEND + "/query", json=payload).json()
    llm = res.get("llm", {})
    st.subheader("Short answer")
    st.write(llm.get("short_answer","(no answer)"))
    st.subheader("Step-by-step")
    st.write(llm.get("step_by_step","(no steps)"))
    st.subheader("Analogy (ELI15)")
    st.write(llm.get("analogy","(no analogy)"))
    st.subheader("Common Errors / Hints")
    st.write(llm.get("common_errors",[]))
    if res.get("diagnosis"):
        st.info(f"Diagnosis: {res['diagnosis']}")

if st.button("Get 5 practice problems"):
    res = requests.post(BACKEND + "/practice", json={}).json()
    for p in res.get("practice", []):
        st.write(f"- {p['id']}: {p['prompt_text']} [{p['topic_tag']}]")
