# LEGSY
Тестовое задание для Legsy socks.  
Телеграм бот принимает от пользователя поисковый запрос и номенклатуру(артикул товара), в ответ получает сообщение. Бот парсит данные с www.wildberries.ru. Если товар находится на первых 100 страницах поиска, присылаете сообщение с номером страницы и позиции, если нет, то любое текстовое сообщение.
#
## Шаблон наполнения env-файла
```
# Токен вашего телеграм бота 
API_TOKEN = 'XXXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
```
## Как запустить проект:

### Опция I (если установлен docker).
Запустить докер контейнер:
```
docker run -d abpdock/legsytest
```

### Опция II.
Клонировать репозиторий и перейти в его директорию Legsy:

```
git clone https://github.com/abp-ce/Legsy.git
cd Legsy
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv

source venv/bin/activate
```

Обновить pip и установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip

pip install -r requirements.txt
```
Запустить проект:

```
python src/telebot.py

```
