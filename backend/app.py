# backend/app.py
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from retrieve_and_prompt import build_prompt
from error_classifier import classify_error
from adaptive_engine import select_next_questions
import json
import random

app = FastAPI()

# placeholder for sending prompt to an LLM
def call_llm(prompt):
    # For demo, return a templated answer using the prompt's retrieved examples.
    # Replace this function with an actual LLM call (HF / OpenAI / local inference).
    # We'll fake a response here for MVP.
    return {
        "short_answer": "See step_by_step",
        "step_by_step": "1) Recognize structure. 2) Solve. (Demo placeholder.)",
        "analogy": "Like stacking blocks.",
        "common_errors": ["arithmetic_mistake", "sign_error"]
    }

class Query(BaseModel):
    question: str
    student_answer: str = None
    student_steps: str = None

@app.post("/query")
def query(q: Query):
    prompt = build_prompt(q.question)
    llm_out = call_llm(prompt)
    # if student answer present, run classifier
    diagnosis = None
    if q.student_answer:
        # attempt to extract numeric expected answer from canonical first retrieved example for demo
        # In prod, compute correct answer or compare with solution generator.
        diagnosis = classify_error(q.student_answer, "demo_correct")  # placeholder
    return {"llm": llm_out, "diagnosis": diagnosis}

@app.post("/practice")
def practice():
    # mock mastery_map - in prod this is per-student
    mastery_map = {}
    picks = select_next_questions(mastery_map, num=5)
    return {"practice": picks}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
