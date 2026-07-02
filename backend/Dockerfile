FROM python:3.11-slim

WORKDIR /app

COPY requirements/base.txt ./requirements/
COPY requirements/dev.txt ./requirements/

RUN pip install --no-cache-dir -r requirements/dev.txt

COPY app ./app
COPY tests ./tests
COPY migrations ./migrations
COPY alembic.ini .
COPY pytest.ini .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]