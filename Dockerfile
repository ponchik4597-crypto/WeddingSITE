FROM python:3.12-slim

RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev --no-install-recommends && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --no-cache-dir django gunicorn pillow

COPY . .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Wedding.wsgi:application"]
