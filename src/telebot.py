import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from dotenv import load_dotenv

import messages as msgs
from constants import CITIES
from decorators import measure_time
from loggers import logger
from wb_parser import parse_query

load_dotenv()
API_TOKEN = os.environ.get('API_TOKEN')

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)

location_db = {}


@dp.message_handler(content_types=['location'])
async def location(message: types.Message):
    global location_db
    lat = message.location.latitude
    lon = message.location.longitude
    location_db[message.chat.id] = (lat, lon,)
    reply = 'Координаты' + msgs.COORD_MESSAGE.format(lat=lat, lon=lon)
    await message.answer(reply, reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands=['city'])
async def choose_city(message: types.Message):
    reply = msgs.CITY_MESSAGE
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for city in CITIES:
        keyboard.add(types.KeyboardButton(city))
    await message.answer(reply, reply_markup=keyboard)


@dp.message_handler(commands=['location'])
async def locate_me(message: types.Message):
    reply = msgs.LOCATION_MESSAGE
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(msgs.LOCATION_BUTTON,
                                  request_location=True)
    keyboard.add(button)
    await message.answer(reply, reply_markup=keyboard)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    global location_db
    reply = (
        f'Привет, {message.from_user.full_name}!\n'
        + msgs.HELP_MESSAGE
    )
    if message.chat.id in location_db:
        reply += '\nВы находитесь:' + msgs.COORD_MESSAGE.format(
            lat=location_db[message.chat.id][0],
            lon=location_db[message.chat.id][1]
        )
    await message.reply(reply)


@dp.message_handler(Text(equals=CITIES))
async def get_city(message: types.Message):
    location_db[message.chat.id] = CITIES[message.text]
    reply = message.text + msgs.COORD_MESSAGE.format(
        lat=CITIES[message.text][0],
        lon=CITIES[message.text][1]
    )
    await message.reply(reply, reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler()
@measure_time
async def wb_parse(message: types.Message):
    logger.info('Пришла строка: ' + message.text)
    answer = msgs.NOT_FOUND_MESSAGE
    words = message.text.split()
    if not words[0].isdigit():
        answer = msgs.NOT_DIGITS_MESSAGE
    else:
        has_location = message.chat.id in location_db
        coords = location_db[message.chat.id] if has_location else None
        page, position, product = parse_query(
            int(words[0]),
            ' '.join(words[1:]),
            coords
        )
        if page != -1:
            answer = msgs.FOUND_MESSAGE.format(
                name=product["name"],
                brand=product["brand"],
                price=product["salePriceU"] / 100,
                page=page,
                position=position
            )
    await message.answer(answer)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
