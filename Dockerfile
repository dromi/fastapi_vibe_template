FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy pyproject.toml and poetry.lock
COPY pyproject.toml poetry.lock ./

# Configure Poetry to install dependencies into the system environment
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-root --no-interaction --no-ansi

# Copy application source
COPY app ./app

# Copy example environment file as .env (for development/demo)
COPY app/.env.example .env

EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
