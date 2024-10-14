FROM python:3.12.7-alpine3.20

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip install --upgrade pip && pip install poetry

RUN poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY . /app/

ENTRYPOINT ["poetry", "run"]
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]