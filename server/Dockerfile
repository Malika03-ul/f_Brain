FROM python:3.13-slim

WORKDIR /app
RUN apt-get update \
    && apt-get install -y build-essential gcc libpq-dev \
    && pip install poetry \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock ./
ENV POETRY_VIRTUALENVS_CREATE=false
RUN poetry install --no-interaction --no-ansi --no-root

COPY . .
CMD ["sh", "-c", "python manage.py migrate && gunicorn ip_converter.wsgi:application --bind 0.0.0.0:8000"]