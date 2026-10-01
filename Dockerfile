FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml README.md database_server.py ./
COPY src ./src

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir .

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/src

EXPOSE 8002

CMD ["python", "database_server.py"]
