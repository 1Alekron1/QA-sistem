import ollama


def get_answer(text: str, question: str) -> str:
    """Формирует запрос к Ollama и возвращает ответ."""
    prompt = f"Есть вопрос: '{question}' \n Ответь на вопрос, по этому тексту '{text}' \n Выводи только ответ, ничего лишнего, если в тексте нет ответа, выведи: В тексте нет ответа на ваш вопрос"
    response = ollama.generate(model="llama3.1", prompt=prompt)
    return response['response']
