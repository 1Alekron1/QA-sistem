from typing import List

def validate_input(text: str, question: str) -> List[str]:
    """Проверяет валидность текста и вопроса, возвращая ошибки, если они есть."""
    errors = []
    if not text.strip():
        errors.append("Text cannot be empty.")
    if not question.strip():
        errors.append("Question cannot be empty.")
    if len(text) > 5000:
        errors.append("Text is too long. Please limit it to 5000 characters.")
    return errors
