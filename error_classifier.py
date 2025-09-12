# error_classifier.py
def classify_error(student_answer, correct_answer, student_steps=None):
    # very simple heuristics for MVP
    try:
        if float(student_answer) == float(correct_answer):
            return "correct"
    except:
        pass
    # arithmetic mismatch: both numeric but not equal
    try:
        float(student_answer)
        float(correct_answer)
        return "arithmetic_mistake"
    except:
        pass
    # algebra form differences
    if "^" in student_answer or "x" in student_answer:
        return "algebra_error"
    return "other"
