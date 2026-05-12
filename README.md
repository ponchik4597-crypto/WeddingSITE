# Wedding Project — Инструкция

## 🛠 Локальная разработка
```bash
# Установка и запуск
pip install django
python manage.py runserver
```

## 🚀 Деплой на сервер (Docker)
```bash
# Загрузка файлов на сервер
scp -r . root@IP:/root/wedding_site

# Сборка и запуск контейнеров
ssh root@IP
cd wedding_site/
docker-compose up -d --build

# Сборка статики (CSS, JS, картинки)
docker-compose exec web python manage.py collectstatic --noinput

# Перезапуск приложения
docker restart wedding-app
```

## 📂 Обновление отдельных файлов (Hotfix)
Если не хочется пересобирать весь контейнер:
```bash
# Шаблоны
scp ./Site/templates/site/presence.html root@IP:/root/wedding_site/Site/templates/site/
# Стили
scp ./Site/static/site/css/presence.css root@IP:/root/wedding_site/Site/static/site/css/
```

## 📊 Работа с базой данных (через Shell)
```bash
# Посмотреть список гостей
docker-compose exec web python manage.py shell -c "from Site.models import Guest; [print(f'Имя: {g.name} | Придет: {g.presence} | С парой: {g.plusone} | Напитки: {g.drink}') for g in Guest.objects.all()]"

# Полная очистка списка гостей
docker-compose exec web python manage.py shell -c "from Site.models import Guest; Guest.objects.all().delete(); print('База очищена')"
```

## 🔑 Права доступа (если БД заблокирована)
```bash
chmod 666 db.sqlite3
chmod 777 .
```

