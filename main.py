from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json


bot = Bot('6885227908:AAHflZ23dvJtiPYOLpTTwVjkqbsTw752N34')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    # markup.add(types.KeyboardButton('Web ilovaga o`tish', web_app=WebAppInfo(url='https://maxway.uz/index.html/')))
    markup.add(types.KeyboardButton('Web ilovaga o`tish', web_app=WebAppInfo(url='https://monkeytype.com/telegram.html/')))

    await message.answer('Bot ishga tushdi', reply_markup=markup)
    


@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f'Ism {res["ism"]}. Email {res["email"]}. Phone {res["phone"]}')

executor.start_polling(dp)