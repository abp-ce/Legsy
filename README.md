# LEGSY
Тестовое задание для Legsy socks.  
Телеграм бот принимает от пользователя поисковый запрос и номенклатуру(артикул товара), в ответ получает сообщение. Бот парсит данные с www.wildberries.ru. Если товар находится на первых 100 страницах поиска, присылаете сообщение с номером страницы и позиции, если нет, то любое текстовое сообщение.
#
### Шаблон наполнения env-файла
```
# Токен вашего телеграм бота 
API_TOKEN = 'XXXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
```
### Как запустить проект:

Клонировать репозиторий и перейти в его директорию infra:

```
git clone https://github.com/abp-ce/foodgram-project-react.git
cd foodgram-project-react/infra
```

Cоздать и запустить докер-контейнеры:

```
docker-compose up -d --build
```

Выполните миграции, соберите статику, создайте суперпользователя,
заполните базу Ingredients:

```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic --no-input
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py populate_db
```