# retrieve_and_prompt.py
import json
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
MODEL = "all-MiniLM-L6-v2"

# load
model = SentenceTransformer(MODEL)
index = faiss.read_index("faiss.index")
with open("data/item_bank.json","r") as f:
    ITEMS = json.load(f)

def retrieve(student_q, k=3):
    q_emb = model.encode([student_q]).astype("float32")
    D, I = index.search(q_emb, k)
    retrieved = [ITEMS[i] for i in I[0]]
    return retrieved

def build_prompt(student_q):
    retrieved = retrieve(student_q, k=3)
    examples = "\n\n".join([f"Q: {r['prompt_text']}\nSolution: {r['solution_text']}" for r in retrieved])
    prompt = f"""You are an SAT Math tutor. A student asks: {student_q}

Use the following worked examples as reference:
{examples}

Return a JSON object with keys:
- short_answer: (final numeric/short result)
- step_by_step: (step by step solution)
- analogy: (one simple analogy for concept)
- common_errors: (list of likely error types and 1-2 hints)

Keep each value concise.
"""
    return prompt
