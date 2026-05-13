# Wedding Project

## Локальная разработка
```bash
# Активация окружения
source .venv/bin/activate

# Установка зависимостей и запуск
pip install -r requirements.txt
python3 manage.py runserver
```

## Деплой на сервер (Docker)
```bash
# Загрузка файлов на сервере
scp -r . root@IP:/root/wedding_site

# Сборка и запуск контейнеров в фоне
ssh root@IP
cd wedding_site/
docker-compose up -d --build

# Сборка статики (CSS, JS, картинки)
docker-compose exec web python manage.py collectstatic --noinput

# Применение миграций базы данных
docker-compose exec web python manage.py migrate

# Перезапуск веб-сервера при необходимости
docker-compose restart web
```

## Обновление отдельных файлов (Hotfix)
Если не хочется пересобирать весь контейнер:
```bash
# Шаблоны
scp ./Site/templates/site/presence.html root@IP:/root/wedding_site/Site/templates/site/
# Стили
scp ./Site/static/site/css/presence.css root@IP:/root/wedding_site/Site/static/site/css/
```

## Работа с базой данных (через Shell)
```bash
# Посмотреть список гостей
docker-compose exec web python manage.py shell -c "from Site.models import Guest; [print(f'Гость: {g}') for g in Guest.objects.all()]"

# Полная очистка списка гостей
docker-compose exec web python manage.py shell -c "from Site.models import Guest; Guest.objects.all().delete(); print('База очищена')"
```

## 🔑 Права доступа
```bash
chmod 666 db.sqlite3
chmod 777 .
```
