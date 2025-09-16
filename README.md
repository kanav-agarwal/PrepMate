# README.md

# SAT Coach — PrepMate

PrepMate is an AI-powered SAT Tutor chatbot designed to help students master SAT problems through step-by-step explanations, adaptive difficulty, and error-specific guidance. Built with Python, Streamlit, and large language models, PrepMate provides a personalized learning experience.

## Features

- **Adaptive Learning:** Tracks student mastery by topic and adjusts difficulty dynamically.
- **Error Classification:** Identifies common mistakes (conceptual, calculation, logic) and provides targeted hints.
- **Step-by-Step Explanations:** Offers detailed solutions, strategies, and alternative approaches.
- **LLM-Powered Guidance:** Uses large language models for natural language explanations and hints.
- **Problem Bank:** Includes curated SAT questions with difficulty tags and topic labels.

## Project Structure

```
├─ LICENSE
├─ README.md
├─ backend/
│  ├─ app.py
│  ├─ adaptive_engine.py
│  ├─ error_classifier.py
│  └─ llm_client.py
├─ frontend/
│  └─ app_ui.py
├─ data/
│  └─ sample_problems.csv
├─ docs/
│  └─ architecture.md
├─ requirements.txt
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/kanav-agarwal/PrepMate.git
cd PrepMate
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Build the question index:
```bash
python backend/build_index.py
```

5. Run the backend server:
```bash
python backend/app.py
```

6. Run the frontend UI:
```bash
streamlit run frontend/app_ui.py
```

## Demo Example

**Input:** `Solve x^2 - 5x + 6 = 0`  
**Bot Output:**  
- **Step 1:** Factor the equation → `(x-2)(x-3)=0`  
- **Step 2:** Solve for x → `x=2 or x=3`  
- **Hint:** Check each solution by substituting back into the original equation  
- **Error Feedback:** If incorrect, identifies whether mistake was in factoring, arithmetic, or logic

*Screenshots of interface and output can be added here.*

## How it Works

1. Student submits a question via frontend.  
2. `backend/app.py` retrieves relevant problems from `data/sample_problems.csv`.  
3. `adaptive_engine.py` selects explanation and difficulty based on mastery level.  
4. `error_classifier.py` analyzes the student’s answer and provides targeted hints.  
5. `llm_client.py` generates natural language explanations using an LLM.  
6. Result is displayed to student in frontend UI.

## Future Improvements

- Replace rule-based error classifier with ML-based classifier using real student data.  
- Implement persistent student tracking for long-term progress and analytics.  
- Integrate more LLMs and allow multiple explanation styles (concise, detailed, analogy).  
- Include real-time quizzes with scoring and mastery metrics.  
- Deploy on cloud for scalable access and multi-user sessions.

## Contribution

- Add more SAT problems with topic and difficulty tags.  
- Improve error classification rules or ML model.  
- Enhance UI for better usability and visualization.

