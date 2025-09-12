# CoachK — SAT Math Tutor (MVP)

## Quick overview
CoachK is an MVP SAT Math tutor with retrieval-augmented explanations, error diagnosis, and adaptive practice.

## Quickstart (local)
1. Create a virtualenv and activate it.
2. `pip install -r requirements.txt`
3. Build the index:
   - `python embed_index.py`
   - This produces `faiss.index` used by the backend.
4. Start the backend:
   - `uvicorn backend.app:app --reload`
5. In another terminal, run frontend:
   - `streamlit run frontend/streamlit_app.py`
6. Open Streamlit UI at `http://localhost:8501`

## Important notes
- `call_llm` in `backend/app.py` is a placeholder. Replace it with your LLM inference:
  - Option A: Hugging Face Inference API
  - Option B: OpenAI Chat API (if allowed by policy)
  - Option C: Local LLM via llama.cpp / vLLM for offline testing
- To improve: implement OCR scratchpad, robust error classifier, student persistence DB, and RL-based adaptive engine.

## How to present in your application
- Add demo gif + link to GitHub repo and short writeup describing the error-diagnosis & adaptive selection innovation.
