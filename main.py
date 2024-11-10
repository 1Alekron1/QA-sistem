from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles  # Добавлено для статических файлов
from services.query_service import get_answer
from services.validation_service import validate_input

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Подключение директории static для CSS и JS файлов
app.mount("/static", StaticFiles(directory="static"), name="static")

last_text = ""

@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    """Отображение главной страницы с полями ввода."""
    global last_text
    return templates.TemplateResponse("index.html", {"request": request, "text": last_text, "errors": None})


@app.post("/ask", response_class=HTMLResponse)
async def ask_question(request: Request, text: str = Form(...), question: str = Form(...)):
    """Обработчик для получения ответа на вопрос."""
    global last_text
    last_text = text  # Сохранение последнего текста, чтобы он оставался при возврате

    # Проверка и валидация ввода
    validation_errors = validate_input(text, question)
    if validation_errors:
        return templates.TemplateResponse("index.html", {"request": request, "text": text, "errors": validation_errors})

    # Получение ответа от модели
    answer = get_answer(text, question)

    # Переадресация на страницу с ответом
    return templates.TemplateResponse("answer.html", {"request": request, "text": text, "question": question, "answer": answer})


@app.get("/new_question", response_class=RedirectResponse)
async def new_question():
    """Возвращение на страницу ввода нового вопроса."""
    return RedirectResponse(url="/")
