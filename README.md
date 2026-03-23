1. pip install django 
2. django-admin startproject Wedding
3. cd Wedding
4. python manage.py runserver
5. ssh root@IP "docker restart wedding-app"
6. scp -r . root@IP:/root/wedding_site загрузка с локального
7. ssh root@IP с сервера
8. cd wedding_site/
9. docker-compose exec web python manage.py collectstatic --noinput
10. docker-compose up -d --build
11. scp ./Site/templates/site/presence.html root@IP:/root/wedding_site/Site/templates/site/ 
12. scp ./Site/static/site/css/presence.css root@IP:/root/wedding_site/Site/static/site/css/
13. docker-compose exec web python manage.py shell -c "from Site.models import Guest; [print(f'Имя: {g.name} | Придет: {g.presence} | С парой: {g.plusone} | Напитки: {g.drink}') for g in Guest.objects.all()]"
14. chmod 666 db.sqlite3
15. chmod 777 .
16. почистить базу docker-compose exec web python manage.py shell -c "from Site.models import Guest; Guest.objects.all().delete(); print('Done')"
