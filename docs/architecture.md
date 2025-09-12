# CoachK Architecture

## Overview

CoachK is designed as a modular SAT Math Tutor chatbot that adapts to student performance, identifies error types, and provides detailed explanations using large language models.

```
User Input → Frontend UI → Backend Server → Retrieval Engine → Adaptive Engine → LLM Client → Error Classifier → Feedback to User
```

## Modules

1. **Frontend (`frontend/app_ui.py`)**  
   - Streamlit-based interface for question submission and response display.  
   - Displays step-by-step solutions, hints, and feedback.

2. **Backend (`backend/app.py`)**  
   - Handles API endpoints and routes between frontend, adaptive engine, LLM, and classifier.  

3. **Adaptive Engine (`backend/adaptive_engine.py`)**  
   - Tracks student mastery by topic and difficulty.  
   - Adjusts problem difficulty and explanation style dynamically.

4. **Error Classifier (`backend/error_classifier.py`)**  
   - Classifies student errors as conceptual, calculation, or logical mistakes.  
   - Provides targeted hints and remediation suggestions.

5. **LLM Client (`backend/llm_client.py`)**  
   - Generates natural language explanations using large language models.  
   - Can be configured to use different LLMs (OpenAI, Hugging Face, etc.)

6. **Data (`data/sample_problems.csv`)**  
   - Contains SAT Math problems with fields: question, solution, topic, difficulty.

## Flow Diagram

```
+------------+       +---------------+       +------------------+
|   Student  | --->  |   Frontend    | --->  |   Backend App    |
+------------+       +---------------+       +------------------+
                                              |       |
                                              v       v
                                     +--------------------+
                                     | Adaptive Engine    |
                                     +--------------------+
                                              |
                                              v
                                     +--------------------+
                                     | Error Classifier   |
                                     +--------------------+
                                              |
                                              v
                                     +--------------------+
                                     | LLM Client         |
                                     +--------------------+
                                              |
                                              v
                                        +------------+
                                        |  Feedback  |
                                        +------------+
```

## Key Features

- Adaptive learning based on topic and mastery.  
- Targeted feedback for student mistakes.  
- Modular architecture allows integration with different LLMs.  
- Scalable backend for future multi-user support.

## Challenges & Limitations

- Current error classifier is rule-based, may miss nuanced student mistakes.  
- Student progress tracking is temporary (in-memory) — needs persistent storage.  
- LLM explanations rely on external APIs; local inference for open-source LLMs is future work.
