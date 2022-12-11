FROM python:3.9-slim

WORKDIR /app

COPY ./requirements.txt /code/requirements.txt

RUN python -m pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . ./

CMD ["python", "src/telebot.py"]