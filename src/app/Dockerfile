FROM python:3.11-slim

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /WEB_APP

RUN pip install poetry

COPY ../pyproject.toml ../poetry.lock* /WEB_APP/

COPY ./src/app ./src/app

RUN poetry install --no-dev --no-cache --no-interaction --no-ansi

CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "80"]
