FROM python:3.12-slim

# установка системных зависимостей для работы с базой
RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev --no-install-recommends && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# остальные файлы проекта
COPY . .

EXPOSE 8000
RUN python manage.py collectstatic --noinput

# запуск через Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Wedding.wsgi:application"]
